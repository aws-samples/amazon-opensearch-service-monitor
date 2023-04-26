'''
# AWS::Comprehend Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_comprehend as comprehend
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Comprehend construct libraries](https://constructs.dev/search?q=comprehend)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Comprehend resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Comprehend.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Comprehend](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Comprehend.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnFlywheel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel",
):
    '''A CloudFormation ``AWS::Comprehend::Flywheel``.

    A flywheel is an AWS resource that orchestrates the ongoing training of a model for custom classification or custom entity recognition. You can create a flywheel to start with an existing trained model, or Comprehend can create and train a new model.

    When you create the flywheel, Comprehend creates a data lake in your account. The data lake holds the training data and test data for all versions of the model.

    To use a flywheel with an existing trained model, you specify the active model version. Comprehend copies the model's training data and test data into the flywheel's data lake.

    To use the flywheel with a new model, you need to provide a dataset for training data (and optional test data) when you create the flywheel.

    For more information about flywheels, see `Flywheel overview <https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html>`_ in the *Amazon Comprehend Developer Guide* .

    :cloudformationResource: AWS::Comprehend::Flywheel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_comprehend as comprehend
        
        cfn_flywheel = comprehend.CfnFlywheel(self, "MyCfnFlywheel",
            data_access_role_arn="dataAccessRoleArn",
            data_lake_s3_uri="dataLakeS3Uri",
            flywheel_name="flywheelName",
        
            # the properties below are optional
            active_model_arn="activeModelArn",
            data_security_config=comprehend.CfnFlywheel.DataSecurityConfigProperty(
                data_lake_kms_key_id="dataLakeKmsKeyId",
                model_kms_key_id="modelKmsKeyId",
                volume_kms_key_id="volumeKmsKeyId",
                vpc_config=comprehend.CfnFlywheel.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            ),
            model_type="modelType",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            task_config=comprehend.CfnFlywheel.TaskConfigProperty(
                language_code="languageCode",
        
                # the properties below are optional
                document_classification_config=comprehend.CfnFlywheel.DocumentClassificationConfigProperty(
                    mode="mode",
        
                    # the properties below are optional
                    labels=["labels"]
                ),
                entity_recognition_config=comprehend.CfnFlywheel.EntityRecognitionConfigProperty(
                    entity_types=[comprehend.CfnFlywheel.EntityTypesListItemProperty(
                        type="type"
                    )]
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_access_role_arn: builtins.str,
        data_lake_s3_uri: builtins.str,
        flywheel_name: builtins.str,
        active_model_arn: typing.Optional[builtins.str] = None,
        data_security_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlywheel.DataSecurityConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        model_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlywheel.TaskConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Comprehend::Flywheel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param data_access_role_arn: The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.
        :param data_lake_s3_uri: Amazon S3 URI of the data lake location.
        :param flywheel_name: Name for the flywheel.
        :param active_model_arn: The Amazon Resource Number (ARN) of the active model version.
        :param data_security_config: Data security configuration.
        :param model_type: Model type of the flywheel's model.
        :param tags: Tags associated with the endpoint being created. A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with "Sales" as the key might be added to an endpoint to indicate its use by the sales department.
        :param task_config: Configuration about the custom classifier associated with the flywheel.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08326dbba3b3e1fbd1b7c33b09deb1212a1a2d4d763f2b2c49693b85d0558b1e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlywheelProps(
            data_access_role_arn=data_access_role_arn,
            data_lake_s3_uri=data_lake_s3_uri,
            flywheel_name=flywheel_name,
            active_model_arn=active_model_arn,
            data_security_config=data_security_config,
            model_type=model_type,
            tags=tags,
            task_config=task_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd5e83f45c4cf44e8697ad9475aa4568fb7e46c1e55467960eb2fbba73831db0)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d874e50f75c45908f76b98c03aedde4475f99a679bf11f72586d1db4114d3c56)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flywheel.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tags associated with the endpoint being created.

        A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with "Sales" as the key might be added to an endpoint to indicate its use by the sales department.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="dataAccessRoleArn")
    def data_access_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-dataaccessrolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "dataAccessRoleArn"))

    @data_access_role_arn.setter
    def data_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6321844bfb2a1d270a9c4a2ca41960fa47c97afa2d07b34a23bdabea326de4ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="dataLakeS3Uri")
    def data_lake_s3_uri(self) -> builtins.str:
        '''Amazon S3 URI of the data lake location.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-datalakes3uri
        '''
        return typing.cast(builtins.str, jsii.get(self, "dataLakeS3Uri"))

    @data_lake_s3_uri.setter
    def data_lake_s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fff80441425e9cd64c92b9e465aff8a17d45193ef5cdfce2238dfa02368ad6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataLakeS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="flywheelName")
    def flywheel_name(self) -> builtins.str:
        '''Name for the flywheel.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-flywheelname
        '''
        return typing.cast(builtins.str, jsii.get(self, "flywheelName"))

    @flywheel_name.setter
    def flywheel_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c532257e2d8a6f8744e338b4f351b10756345f6375da4dfa2cd7d6c070693a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flywheelName", value)

    @builtins.property
    @jsii.member(jsii_name="activeModelArn")
    def active_model_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Number (ARN) of the active model version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-activemodelarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activeModelArn"))

    @active_model_arn.setter
    def active_model_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a83eb6aee874a71ef2102b785b12cf1d675f7af5d375d9a5440d9a3e8326938)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeModelArn", value)

    @builtins.property
    @jsii.member(jsii_name="dataSecurityConfig")
    def data_security_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.DataSecurityConfigProperty"]]:
        '''Data security configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-datasecurityconfig
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.DataSecurityConfigProperty"]], jsii.get(self, "dataSecurityConfig"))

    @data_security_config.setter
    def data_security_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.DataSecurityConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd6d966515c5a7a9a270dde08d7f0431bd24b3c8ab2bf5c260c0fdd300d5b85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSecurityConfig", value)

    @builtins.property
    @jsii.member(jsii_name="modelType")
    def model_type(self) -> typing.Optional[builtins.str]:
        '''Model type of the flywheel's model.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-modeltype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelType"))

    @model_type.setter
    def model_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__514af0a34ecf2e72cd065a5b350ad942f9e94663e6471b9b89fdd65f9b7916e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelType", value)

    @builtins.property
    @jsii.member(jsii_name="taskConfig")
    def task_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.TaskConfigProperty"]]:
        '''Configuration about the custom classifier associated with the flywheel.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-taskconfig
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.TaskConfigProperty"]], jsii.get(self, "taskConfig"))

    @task_config.setter
    def task_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.TaskConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0986d76e0fdf3e18c2b4c799702f67afa8cf1195e0284e9e6d264962d96deda0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel.DataSecurityConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_lake_kms_key_id": "dataLakeKmsKeyId",
            "model_kms_key_id": "modelKmsKeyId",
            "volume_kms_key_id": "volumeKmsKeyId",
            "vpc_config": "vpcConfig",
        },
    )
    class DataSecurityConfigProperty:
        def __init__(
            self,
            *,
            data_lake_kms_key_id: typing.Optional[builtins.str] = None,
            model_kms_key_id: typing.Optional[builtins.str] = None,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
            vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlywheel.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Data security configuration.

            :param data_lake_kms_key_id: ID for the AWS KMS key that Amazon Comprehend uses to encrypt the data in the data lake.
            :param model_kms_key_id: ID for the AWS KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats: - KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"`` - Amazon Resource Name (ARN) of a KMS Key: ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``
            :param volume_kms_key_id: ID for the AWS KMS key that Amazon Comprehend uses to encrypt the volume.
            :param vpc_config: Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job. For more information, see `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                data_security_config_property = comprehend.CfnFlywheel.DataSecurityConfigProperty(
                    data_lake_kms_key_id="dataLakeKmsKeyId",
                    model_kms_key_id="modelKmsKeyId",
                    volume_kms_key_id="volumeKmsKeyId",
                    vpc_config=comprehend.CfnFlywheel.VpcConfigProperty(
                        security_group_ids=["securityGroupIds"],
                        subnets=["subnets"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ff8373493505a153def3a8e5139b9d9d48859656b3e590520f078b93a19d00df)
                check_type(argname="argument data_lake_kms_key_id", value=data_lake_kms_key_id, expected_type=type_hints["data_lake_kms_key_id"])
                check_type(argname="argument model_kms_key_id", value=model_kms_key_id, expected_type=type_hints["model_kms_key_id"])
                check_type(argname="argument volume_kms_key_id", value=volume_kms_key_id, expected_type=type_hints["volume_kms_key_id"])
                check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data_lake_kms_key_id is not None:
                self._values["data_lake_kms_key_id"] = data_lake_kms_key_id
            if model_kms_key_id is not None:
                self._values["model_kms_key_id"] = model_kms_key_id
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def data_lake_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''ID for the AWS KMS key that Amazon Comprehend uses to encrypt the data in the data lake.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html#cfn-comprehend-flywheel-datasecurityconfig-datalakekmskeyid
            '''
            result = self._values.get("data_lake_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def model_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''ID for the AWS KMS key that Amazon Comprehend uses to encrypt trained custom models.

            The ModelKmsKeyId can be either of the following formats:

            - KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``
            - Amazon Resource Name (ARN) of a KMS Key: ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html#cfn-comprehend-flywheel-datasecurityconfig-modelkmskeyid
            '''
            result = self._values.get("model_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''ID for the AWS KMS key that Amazon Comprehend uses to encrypt the volume.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html#cfn-comprehend-flywheel-datasecurityconfig-volumekmskeyid
            '''
            result = self._values.get("volume_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.VpcConfigProperty"]]:
            '''Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job.

            For more information, see `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html#cfn-comprehend-flywheel-datasecurityconfig-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSecurityConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel.DocumentClassificationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode", "labels": "labels"},
    )
    class DocumentClassificationConfigProperty:
        def __init__(
            self,
            *,
            mode: builtins.str,
            labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Configuration required for a custom classification model.

            :param mode: Classification mode indicates whether the documents are ``MULTI_CLASS`` or ``MULTI_LABEL`` .
            :param labels: One or more labels to associate with the custom classifier.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-documentclassificationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                document_classification_config_property = comprehend.CfnFlywheel.DocumentClassificationConfigProperty(
                    mode="mode",
                
                    # the properties below are optional
                    labels=["labels"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0208591bc4eb6449ba2ec94d642467202e116283b6b07af3dcf486c7ac51e82a)
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
                check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mode": mode,
            }
            if labels is not None:
                self._values["labels"] = labels

        @builtins.property
        def mode(self) -> builtins.str:
            '''Classification mode indicates whether the documents are ``MULTI_CLASS`` or ``MULTI_LABEL`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-documentclassificationconfig.html#cfn-comprehend-flywheel-documentclassificationconfig-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def labels(self) -> typing.Optional[typing.List[builtins.str]]:
            '''One or more labels to associate with the custom classifier.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-documentclassificationconfig.html#cfn-comprehend-flywheel-documentclassificationconfig-labels
            '''
            result = self._values.get("labels")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentClassificationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel.EntityRecognitionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"entity_types": "entityTypes"},
    )
    class EntityRecognitionConfigProperty:
        def __init__(
            self,
            *,
            entity_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlywheel.EntityTypesListItemProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration required for an entity recognition model.

            :param entity_types: Up to 25 entity types that the model is trained to recognize.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entityrecognitionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                entity_recognition_config_property = comprehend.CfnFlywheel.EntityRecognitionConfigProperty(
                    entity_types=[comprehend.CfnFlywheel.EntityTypesListItemProperty(
                        type="type"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be861f74134a724bbb961275d90cd0dc1f9f6a80ba3ad69a6dd1d2865df480b1)
                check_type(argname="argument entity_types", value=entity_types, expected_type=type_hints["entity_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if entity_types is not None:
                self._values["entity_types"] = entity_types

        @builtins.property
        def entity_types(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.EntityTypesListItemProperty"]]]]:
            '''Up to 25 entity types that the model is trained to recognize.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entityrecognitionconfig.html#cfn-comprehend-flywheel-entityrecognitionconfig-entitytypes
            '''
            result = self._values.get("entity_types")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.EntityTypesListItemProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntityRecognitionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel.EntityTypesListItemProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type"},
    )
    class EntityTypesListItemProperty:
        def __init__(self, *, type: builtins.str) -> None:
            '''An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.

            :param type: An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer. Entity types must not contain the following invalid characters: \\n (line break), \\n (escaped line break, \\r (carriage return), \\r (escaped carriage return), \\t (tab), \\t (escaped tab), space, and , (comma).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entitytypeslistitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                entity_types_list_item_property = comprehend.CfnFlywheel.EntityTypesListItemProperty(
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__92a4eeaf2d69acccc3b3d8d1d0551ae8552d2bf97966201e3ec32e4a8af8c8bf)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.

            Entity types must not contain the following invalid characters: \\n (line break), \\n (escaped line break, \\r (carriage return), \\r (escaped carriage return), \\t (tab), \\t (escaped tab), space, and , (comma).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entitytypeslistitem.html#cfn-comprehend-flywheel-entitytypeslistitem-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntityTypesListItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel.TaskConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "language_code": "languageCode",
            "document_classification_config": "documentClassificationConfig",
            "entity_recognition_config": "entityRecognitionConfig",
        },
    )
    class TaskConfigProperty:
        def __init__(
            self,
            *,
            language_code: builtins.str,
            document_classification_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlywheel.DocumentClassificationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            entity_recognition_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlywheel.EntityRecognitionConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration about the custom classifier associated with the flywheel.

            :param language_code: Language code for the language that the model supports.
            :param document_classification_config: Configuration required for a classification model.
            :param entity_recognition_config: Configuration required for an entity recognition model.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                task_config_property = comprehend.CfnFlywheel.TaskConfigProperty(
                    language_code="languageCode",
                
                    # the properties below are optional
                    document_classification_config=comprehend.CfnFlywheel.DocumentClassificationConfigProperty(
                        mode="mode",
                
                        # the properties below are optional
                        labels=["labels"]
                    ),
                    entity_recognition_config=comprehend.CfnFlywheel.EntityRecognitionConfigProperty(
                        entity_types=[comprehend.CfnFlywheel.EntityTypesListItemProperty(
                            type="type"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b33cd312cecdc06a8bdf8295b58c64bf16dac30f37454b9584e214a7a169c56)
                check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
                check_type(argname="argument document_classification_config", value=document_classification_config, expected_type=type_hints["document_classification_config"])
                check_type(argname="argument entity_recognition_config", value=entity_recognition_config, expected_type=type_hints["entity_recognition_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "language_code": language_code,
            }
            if document_classification_config is not None:
                self._values["document_classification_config"] = document_classification_config
            if entity_recognition_config is not None:
                self._values["entity_recognition_config"] = entity_recognition_config

        @builtins.property
        def language_code(self) -> builtins.str:
            '''Language code for the language that the model supports.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html#cfn-comprehend-flywheel-taskconfig-languagecode
            '''
            result = self._values.get("language_code")
            assert result is not None, "Required property 'language_code' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_classification_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.DocumentClassificationConfigProperty"]]:
            '''Configuration required for a classification model.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html#cfn-comprehend-flywheel-taskconfig-documentclassificationconfig
            '''
            result = self._values.get("document_classification_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.DocumentClassificationConfigProperty"]], result)

        @builtins.property
        def entity_recognition_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.EntityRecognitionConfigProperty"]]:
            '''Configuration required for an entity recognition model.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html#cfn-comprehend-flywheel-taskconfig-entityrecognitionconfig
            '''
            result = self._values.get("entity_recognition_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.EntityRecognitionConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job.

            For more information, see `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`_ .

            :param security_group_ids: The ID number for a security group on an instance of your private VPC. Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that you’ll be accessing on the VPC. This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ .
            :param subnets: The ID for each subnet being used in your private VPC. This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s Region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                vpc_config_property = comprehend.CfnFlywheel.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6f148a8e29a057dfa8bd6a5945aaf37e92f70297900e6a35e12b4f9de104ca70)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''The ID number for a security group on an instance of your private VPC.

            Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that you’ll be accessing on the VPC. This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-vpcconfig.html#cfn-comprehend-flywheel-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''The ID for each subnet being used in your private VPC.

            This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s Region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-vpcconfig.html#cfn-comprehend-flywheel-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheelProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_access_role_arn": "dataAccessRoleArn",
        "data_lake_s3_uri": "dataLakeS3Uri",
        "flywheel_name": "flywheelName",
        "active_model_arn": "activeModelArn",
        "data_security_config": "dataSecurityConfig",
        "model_type": "modelType",
        "tags": "tags",
        "task_config": "taskConfig",
    },
)
class CfnFlywheelProps:
    def __init__(
        self,
        *,
        data_access_role_arn: builtins.str,
        data_lake_s3_uri: builtins.str,
        flywheel_name: builtins.str,
        active_model_arn: typing.Optional[builtins.str] = None,
        data_security_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.DataSecurityConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        model_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.TaskConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFlywheel``.

        :param data_access_role_arn: The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.
        :param data_lake_s3_uri: Amazon S3 URI of the data lake location.
        :param flywheel_name: Name for the flywheel.
        :param active_model_arn: The Amazon Resource Number (ARN) of the active model version.
        :param data_security_config: Data security configuration.
        :param model_type: Model type of the flywheel's model.
        :param tags: Tags associated with the endpoint being created. A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with "Sales" as the key might be added to an endpoint to indicate its use by the sales department.
        :param task_config: Configuration about the custom classifier associated with the flywheel.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_comprehend as comprehend
            
            cfn_flywheel_props = comprehend.CfnFlywheelProps(
                data_access_role_arn="dataAccessRoleArn",
                data_lake_s3_uri="dataLakeS3Uri",
                flywheel_name="flywheelName",
            
                # the properties below are optional
                active_model_arn="activeModelArn",
                data_security_config=comprehend.CfnFlywheel.DataSecurityConfigProperty(
                    data_lake_kms_key_id="dataLakeKmsKeyId",
                    model_kms_key_id="modelKmsKeyId",
                    volume_kms_key_id="volumeKmsKeyId",
                    vpc_config=comprehend.CfnFlywheel.VpcConfigProperty(
                        security_group_ids=["securityGroupIds"],
                        subnets=["subnets"]
                    )
                ),
                model_type="modelType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                task_config=comprehend.CfnFlywheel.TaskConfigProperty(
                    language_code="languageCode",
            
                    # the properties below are optional
                    document_classification_config=comprehend.CfnFlywheel.DocumentClassificationConfigProperty(
                        mode="mode",
            
                        # the properties below are optional
                        labels=["labels"]
                    ),
                    entity_recognition_config=comprehend.CfnFlywheel.EntityRecognitionConfigProperty(
                        entity_types=[comprehend.CfnFlywheel.EntityTypesListItemProperty(
                            type="type"
                        )]
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__354388f245744b59494c23dd6a47939e13228c4105132c6911824acf04080c64)
            check_type(argname="argument data_access_role_arn", value=data_access_role_arn, expected_type=type_hints["data_access_role_arn"])
            check_type(argname="argument data_lake_s3_uri", value=data_lake_s3_uri, expected_type=type_hints["data_lake_s3_uri"])
            check_type(argname="argument flywheel_name", value=flywheel_name, expected_type=type_hints["flywheel_name"])
            check_type(argname="argument active_model_arn", value=active_model_arn, expected_type=type_hints["active_model_arn"])
            check_type(argname="argument data_security_config", value=data_security_config, expected_type=type_hints["data_security_config"])
            check_type(argname="argument model_type", value=model_type, expected_type=type_hints["model_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_config", value=task_config, expected_type=type_hints["task_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_access_role_arn": data_access_role_arn,
            "data_lake_s3_uri": data_lake_s3_uri,
            "flywheel_name": flywheel_name,
        }
        if active_model_arn is not None:
            self._values["active_model_arn"] = active_model_arn
        if data_security_config is not None:
            self._values["data_security_config"] = data_security_config
        if model_type is not None:
            self._values["model_type"] = model_type
        if tags is not None:
            self._values["tags"] = tags
        if task_config is not None:
            self._values["task_config"] = task_config

    @builtins.property
    def data_access_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-dataaccessrolearn
        '''
        result = self._values.get("data_access_role_arn")
        assert result is not None, "Required property 'data_access_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_lake_s3_uri(self) -> builtins.str:
        '''Amazon S3 URI of the data lake location.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-datalakes3uri
        '''
        result = self._values.get("data_lake_s3_uri")
        assert result is not None, "Required property 'data_lake_s3_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flywheel_name(self) -> builtins.str:
        '''Name for the flywheel.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-flywheelname
        '''
        result = self._values.get("flywheel_name")
        assert result is not None, "Required property 'flywheel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_model_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Number (ARN) of the active model version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-activemodelarn
        '''
        result = self._values.get("active_model_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_security_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlywheel.DataSecurityConfigProperty]]:
        '''Data security configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-datasecurityconfig
        '''
        result = self._values.get("data_security_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlywheel.DataSecurityConfigProperty]], result)

    @builtins.property
    def model_type(self) -> typing.Optional[builtins.str]:
        '''Model type of the flywheel's model.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-modeltype
        '''
        result = self._values.get("model_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags associated with the endpoint being created.

        A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with "Sales" as the key might be added to an endpoint to indicate its use by the sales department.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def task_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlywheel.TaskConfigProperty]]:
        '''Configuration about the custom classifier associated with the flywheel.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-taskconfig
        '''
        result = self._values.get("task_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlywheel.TaskConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlywheelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnFlywheel",
    "CfnFlywheelProps",
]

publication.publish()

def _typecheckingstub__08326dbba3b3e1fbd1b7c33b09deb1212a1a2d4d763f2b2c49693b85d0558b1e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_access_role_arn: builtins.str,
    data_lake_s3_uri: builtins.str,
    flywheel_name: builtins.str,
    active_model_arn: typing.Optional[builtins.str] = None,
    data_security_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.DataSecurityConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    model_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.TaskConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd5e83f45c4cf44e8697ad9475aa4568fb7e46c1e55467960eb2fbba73831db0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d874e50f75c45908f76b98c03aedde4475f99a679bf11f72586d1db4114d3c56(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6321844bfb2a1d270a9c4a2ca41960fa47c97afa2d07b34a23bdabea326de4ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fff80441425e9cd64c92b9e465aff8a17d45193ef5cdfce2238dfa02368ad6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c532257e2d8a6f8744e338b4f351b10756345f6375da4dfa2cd7d6c070693a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a83eb6aee874a71ef2102b785b12cf1d675f7af5d375d9a5440d9a3e8326938(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fd6d966515c5a7a9a270dde08d7f0431bd24b3c8ab2bf5c260c0fdd300d5b85(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlywheel.DataSecurityConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__514af0a34ecf2e72cd065a5b350ad942f9e94663e6471b9b89fdd65f9b7916e2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0986d76e0fdf3e18c2b4c799702f67afa8cf1195e0284e9e6d264962d96deda0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlywheel.TaskConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff8373493505a153def3a8e5139b9d9d48859656b3e590520f078b93a19d00df(
    *,
    data_lake_kms_key_id: typing.Optional[builtins.str] = None,
    model_kms_key_id: typing.Optional[builtins.str] = None,
    volume_kms_key_id: typing.Optional[builtins.str] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0208591bc4eb6449ba2ec94d642467202e116283b6b07af3dcf486c7ac51e82a(
    *,
    mode: builtins.str,
    labels: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be861f74134a724bbb961275d90cd0dc1f9f6a80ba3ad69a6dd1d2865df480b1(
    *,
    entity_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.EntityTypesListItemProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a4eeaf2d69acccc3b3d8d1d0551ae8552d2bf97966201e3ec32e4a8af8c8bf(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b33cd312cecdc06a8bdf8295b58c64bf16dac30f37454b9584e214a7a169c56(
    *,
    language_code: builtins.str,
    document_classification_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.DocumentClassificationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    entity_recognition_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.EntityRecognitionConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f148a8e29a057dfa8bd6a5945aaf37e92f70297900e6a35e12b4f9de104ca70(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnets: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__354388f245744b59494c23dd6a47939e13228c4105132c6911824acf04080c64(
    *,
    data_access_role_arn: builtins.str,
    data_lake_s3_uri: builtins.str,
    flywheel_name: builtins.str,
    active_model_arn: typing.Optional[builtins.str] = None,
    data_security_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.DataSecurityConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    model_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.TaskConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
