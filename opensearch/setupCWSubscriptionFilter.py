#!/usr/bin/python
'''
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
'''
import boto3
import json
import sys

if (len(sys.argv) != 2):
    sys.exit("Incorrect argument, please run as python3 setupCWSubscriptionFilter.py deploy|destroy ")

# This variable gets replaced as per opensearch_monitor_stack.py#REGIONS_TO_MONITOR everytime cdk deploy/destroy kicks in
REGIONS_TO_MONITOR='["us-east-1", "us-east-2", "us-west-1", "us-west-2", "ap-south-1", "ap-northeast-1", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "sa-east-1"]'

session = boto3.session.Session()
current_region = session.region_name
account_id = boto3.client("sts").get_caller_identity()["Account"]
# Prefix to define CW Log group which need to be traversed and create/delete subscription filter for same
logGroupNamePrefixAES='/aws/aes/domains'
logGroupNamePrefixOpensearch='/aws/OpenSearchService/domains'
subscriptionFilterNamePrefix='OpenSearch-CWLogs-filter-'

def deploy(cwLogGroupPrefix):
    # Create subscription filter for all CW Logs across regions for Amazon OpenSearch Service 
    for region in json.loads(REGIONS_TO_MONITOR):
        print("Starting to create CW Log filters for", region)
        # Create CW Logs client
        cw_logs_client = boto3.client('logs', region_name=region)
        response = cw_logs_client.describe_log_groups(
            logGroupNamePrefix=cwLogGroupPrefix
        )
        # Read response which is dict, and change that to json with quotes "
        json_response = json.dumps(response)

        # Parse JSON data to extract logGroups
        log_groups = json.loads(json_response)["logGroups"]
        for log_group in log_groups:
            print("Processing logGroups:", log_group["arn"])
            cw_logs_client.put_subscription_filter(
                logGroupName=log_group["logGroupName"],
                filterName=subscriptionFilterNamePrefix + log_group["logGroupName"] + "-" + region,
                filterPattern=' ',
                destinationArn='arn:aws:lambda:' + current_region + ':' + account_id + ':function:CWLogsToOpenSearch_monitoring'
            )


def destroy(cwLogGroupPrefix):
    # Delete subscription filter from all CW Logs across regions for Amazon OpenSearch Service
    for region in json.loads(REGIONS_TO_MONITOR):
        print("Starting to delete CW Log filters for", region)
        # Create CW Logs client
        cw_logs_client = boto3.client('logs', region_name=region)
        response = cw_logs_client.describe_log_groups(
            logGroupNamePrefix=cwLogGroupPrefix
        )
        # Read response which is dict, and change that to json with "
        json_response = json.dumps(response)

        # Parse JSON data to extract logGroups
        log_groups = json.loads(json_response)["logGroups"]
        # Traverse each log group to list cw logs filter and delete the one starting with 'subscriptionFilterNamePrefix'
        for log_group in log_groups:
            print("Processing logGroups:", log_group["arn"])
            filter_response = cw_logs_client.describe_subscription_filters(
                logGroupName=log_group["logGroupName"],
                filterNamePrefix=subscriptionFilterNamePrefix
            )
            # Read response which is dict, and change that to json with quotes "
            filter_json_response = json.dumps(filter_response)
            subscription_filters = json.loads(filter_json_response)["subscriptionFilters"]

            # Iterate subscriptionFilter to delete
            for filter in subscription_filters:
                print("Deleting subscriptionFilter:", filter["filterName"])
                cw_logs_client.delete_subscription_filter(
                    logGroupName=log_group["logGroupName"],
                    filterName=filter["filterName"]
                )


if (sys.argv[1].lower() == "deploy"):
    # Can be removed in future major version when Amazon ES is deprecated
    deploy(logGroupNamePrefixAES)
    deploy(logGroupNamePrefixOpensearch)

elif (sys.argv[1].lower() == "destroy"):
    # Can be removed in future major version when Amazon ES is deprecated
    destroy(logGroupNamePrefixAES)
    destroy(logGroupNamePrefixOpensearch)

else:
    sys.exit("Unrecognised argument '" + sys.argv[1].lower() + "', please run as python3 setupCWSubscriptionFilter.py deploy|destroy ")


