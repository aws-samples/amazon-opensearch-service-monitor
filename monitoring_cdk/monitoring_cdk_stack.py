'''
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
'''

from aws_cdk import (
    aws_dynamodb as ddb,
    aws_elasticsearch as es,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,
    aws_lambda as lambda_,
    aws_ec2 as ec2,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,    
    core
)
import os.path
from aws_cdk.aws_s3_assets import Asset


# Jump host specific settings, change key name if you need an existing key to be used
EC2_KEY_NAME='aes_cdk_monitoring'
EC2_INSTANCE_TYPE='t3.nano'

# Fill this in with a valid email to receive SNS notifications.
SNS_NOTIFICATION_EMAIL='user@example.com'

# Lambda Interval Settings (seconds)
LAMBDA_INTERVAL=300

# Elasticsearch and Kibana specific constants 
DOMAIN_NAME = 'aes-cdk-monitoring'
DOMAIN_ADMIN_UNAME='admin'
DOMAIN_ADMIN_PW='Kibana123!'
DOMAIN_DATA_NODE_INSTANCE_TYPE='t3.medium.elasticsearch'
DOMAIN_DATA_NODE_INSTANCE_COUNT=2
DOMAIN_INSTANCE_VOLUME_SIZE=100
DOMAIN_AZ_COUNT=2
REGIONS_TO_MONITOR='["us-east-1", "us-east-2", "us-west-1", "us-west-2", "af-south-1", "ap-east-1", "ap-south-1", "ap-northeast-1", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "eu-south-1", "me-south-1",   "sa-east-1"]'

## By default monitoring stack will be setup without dedicated master node, to have dedicated master node in stack do change the number of nodes and type (if needed)
## Maximum Master Instance count supported by service is 5, so either have 3 or 5 dedicated node for master
DOMAIN_MASTER_NODE_INSTANCE_TYPE='t3.medium.elasticsearch'
DOMAIN_MASTER_NODE_INSTANCE_COUNT=0

## To enable UW, please make master node count as 3 or 5, and UW node count as minimum 2
## Also change data node to be non T2/T3 as UW does not support T2/T3 as data nodes
DOMAIN_UW_NODE_INSTANCE_TYPE='ultrawarm1.medium.elasticsearch'
DOMAIN_UW_NODE_INSTANCE_COUNT=0

# DDB settings
TABLE_NAME = 'timestamps'

class MonitoringCdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        ################################################################################
        # VPC
        vpc = ec2.Vpc(self, "Monitoring VPC", max_azs=3)

        ################################################################################
        # Amazon ES domain
        # TODO: Add a template and ISM to the domain
        es_sec_grp = ec2.SecurityGroup(self, 'ESSecGrpMonitoring', 
                                        vpc=vpc,
                                        allow_all_outbound=True,
                                        security_group_name='ESSecGrpMonitoring')
        es_sec_grp.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80))
        es_sec_grp.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(443))

        domain = es.Domain(self, 'cdk-monitoring-domain', 
                    version=es.ElasticsearchVersion.of('7.10'), # Upgrade when CDK upgrades
                    domain_name=DOMAIN_NAME,
                    capacity=es.CapacityConfig(data_node_instance_type=DOMAIN_DATA_NODE_INSTANCE_TYPE,
                                                data_nodes=DOMAIN_DATA_NODE_INSTANCE_COUNT,
                                                master_node_instance_type=DOMAIN_MASTER_NODE_INSTANCE_TYPE,
                                                master_nodes=DOMAIN_MASTER_NODE_INSTANCE_COUNT,
                                                warm_instance_type=DOMAIN_UW_NODE_INSTANCE_TYPE,
                                                warm_nodes=DOMAIN_UW_NODE_INSTANCE_COUNT
                                            ),
                    ebs=es.EbsOptions(enabled=True,
                                        volume_size=DOMAIN_INSTANCE_VOLUME_SIZE,
                                        volume_type=ec2.EbsDeviceVolumeType.GP2),
                    vpc_options=es.VpcOptions(
                        security_groups=[es_sec_grp],
                        subnets=vpc.public_subnets,
                    ),
                    zone_awareness=es.ZoneAwarenessConfig(enabled=True,
                                                          availability_zone_count=DOMAIN_AZ_COUNT),
                    enforce_https=True,
                    node_to_node_encryption=True,
                    encryption_at_rest={
                        "enabled": True
                    },
                    use_unsigned_basic_auth=True,
                    fine_grained_access_control={
                        "master_user_name": DOMAIN_ADMIN_UNAME,
                        "master_user_password": core.SecretValue.plain_text(DOMAIN_ADMIN_PW)
                    },
                 )

        core.CfnOutput(self, "MasterPW",
                        value=DOMAIN_ADMIN_PW,
                        description="Master User Password for Amazon ES domain")


        ################################################################################
        # Dynamo DB table for time stamp tracking
        table = ddb.Table(self, 'monitoring-lambda-timestamp',
                          table_name=TABLE_NAME,
                          partition_key=ddb.Attribute(
                                name="domain",
                                type=ddb.AttributeType.STRING
                          ),
                          sort_key=ddb.Attribute(
                              name='region',
                              type=ddb.AttributeType.STRING
                          ),
                          removal_policy=core.RemovalPolicy.DESTROY
                        )

        ################################################################################
        # Lambda monitoring function
        lambda_func = lambda_.Function(
            self, 'handler',
            runtime = lambda_.Runtime.PYTHON_3_8,
            code=lambda_.Code.asset('monitoring-py'),
            handler='handler.handler',
            memory_size=1024,
            timeout=core.Duration.minutes(10),
            vpc=vpc
        )

        table.grant_read_data(lambda_func)
        table.grant_write_data(lambda_func)
        lambda_func.add_environment('TABLE', table.table_name)
        lambda_func.add_environment('DOMAIN_ENDPOINT', 'https://' + domain.domain_endpoint)
        lambda_func.add_environment('DOMAIN_ADMIN_UNAME', DOMAIN_ADMIN_UNAME)
        lambda_func.add_environment('DOMAIN_ADMIN_PW', DOMAIN_ADMIN_PW)
        lambda_func.add_environment('REGIONS', REGIONS_TO_MONITOR)

        # When the domain is created here, restrict access
        lambda_func.add_to_role_policy(iam.PolicyStatement(actions=['es:*'],
            resources=['*']))

        # The function needs to read CW events. Restrict
        lambda_func.add_to_role_policy(iam.PolicyStatement(actions=['cloudwatch:*'],
            resources=['*']))

        lambda_schedule = events.Schedule.rate(core.Duration.seconds(LAMBDA_INTERVAL))
        event_lambda_target = targets.LambdaFunction(handler=lambda_func)
        events.Rule(
            self,
            "Monitoring",
            enabled=True,
            schedule=lambda_schedule,
            targets=[event_lambda_target])

        ################################################################################
        # Jump host for SSH tunneling and direct access
        sn_public = ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
 
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
            )
 
        # Instance Role and SSM Managed Policy
        role = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonEC2RoleforSSM"))
 
        instance = ec2.Instance(self, 'instance',
                                instance_type=ec2.InstanceType(EC2_INSTANCE_TYPE),
                                vpc=vpc,
                                machine_image=amzn_linux,
                                vpc_subnets=sn_public,
                                key_name=EC2_KEY_NAME,
                                role=role,
                                )
        instance.connections.allow_from_any_ipv4(ec2.Port.tcp(22), 'SSH')
        instance.connections.allow_from_any_ipv4(ec2.Port.tcp(443), 'HTTPS')
 
        stmt = iam.PolicyStatement(actions=['es:*'],
                                   resources=[domain.domain_arn])
        instance.add_to_role_policy(stmt)

        # Create SNS topic, subscription, IAM roles, Policies
        sns_topic = sns.Topic(self, "cdk_monitoring_topic")

        sns_topic.add_subscription(subscriptions.EmailSubscription(SNS_NOTIFICATION_EMAIL))

        sns_policy_statement=iam.PolicyStatement(
                actions=["sns:publish"],
                resources=[sns_topic.topic_arn],
                effect=iam.Effect.ALLOW
        )
        sns_policy = iam.ManagedPolicy(self, "cdk_monitoring_policy")
        sns_policy.add_statements(sns_policy_statement)

        sns_role = iam.Role(self, "cdk_monitoring_sns_role", 
            assumed_by=iam.ServicePrincipal("es.amazonaws.com")
        )
        sns_role.add_managed_policy(sns_policy)

        dirname = os.path.dirname(__file__)
        kibana_asset = Asset(self, "KibanaAsset", path=os.path.join(dirname, 'export_kibana_dashboards_V7_9.ndjson'))
        kibana_asset.grant_read(instance.role)
        kibana_asset_path = instance.user_data.add_s3_download_command(
            bucket=kibana_asset.bucket,
            bucket_key=kibana_asset.s3_object_key,
        )

        nginx_asset = Asset(self, "NginxAsset", path=os.path.join(dirname, 'nginx_kibana.conf'))
        nginx_asset.grant_read(instance.role)
        nginx_asset_path = instance.user_data.add_s3_download_command(
            bucket=nginx_asset.bucket,
            bucket_key=nginx_asset.s3_object_key,
        )

        alerting_asset = Asset(self, "AlertingAsset", path=os.path.join(dirname, 'create_alerts.sh'))
        alerting_asset.grant_read(instance.role)
        alerting_asset_path = instance.user_data.add_s3_download_command(
            bucket=alerting_asset.bucket,
            bucket_key=alerting_asset.s3_object_key,
        )


        instance.user_data.add_commands(
            "yum update -y",
            "yum install jq -y",
            "amazon-linux-extras install nginx1.12",
            "cd /tmp/assets",
            "mv {} export_kibana_dashboards_V7_9.ndjson".format(kibana_asset_path),
            "mv {} nginx_kibana.conf".format(nginx_asset_path),
            "mv {} create_alerts.sh".format(alerting_asset_path),

            "openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/cert.key -out /etc/nginx/cert.crt -subj /C=US/ST=./L=./O=./CN=.\n"
            "cp nginx_kibana.conf /etc/nginx/conf.d/",
            "sed -i 's/DOMAIN_ENDPOINT/" + domain.domain_endpoint + "/g' /etc/nginx/conf.d/nginx_kibana.conf",
            "sed -i 's/DOMAIN_ENDPOINT/" + domain.domain_endpoint + "/g' /tmp/assets/create_alerts.sh",
            "sed -i 's=SNS_ROLE_ARN=" + sns_role.role_arn + "=g' /tmp/assets/create_alerts.sh",
            "sed -i 's/SNS_TOPIC_ARN/" + sns_topic.topic_arn + "/g' /tmp/assets/create_alerts.sh",
            "sed -i 's=DOMAIN_ADMIN_UNAME=" + DOMAIN_ADMIN_UNAME + "=g' /tmp/assets/create_alerts.sh",
            "sed -i 's=DOMAIN_ADMIN_PW=" + DOMAIN_ADMIN_PW + "=g' /tmp/assets/create_alerts.sh",
            
            "systemctl restart nginx.service",
            "chmod 500 create_alerts.sh",
            "sleep 5",
            "bash --verbose create_alerts.sh",
        )

        core.CfnOutput(self, "Kibana URL (via Jump host)",
                        value="https://" + instance.instance_public_ip,
                        description="Kibana URL via Jump host")

        core.CfnOutput(self, "SNS Subscription Alert Message",
                        value=SNS_NOTIFICATION_EMAIL,
                        description="Please confirm your SNS subscription receievedt at")



