'''
# AWS::InternetMonitor Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_internetmonitor as internetmonitor
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for InternetMonitor construct libraries](https://constructs.dev/search?q=internetmonitor)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::InternetMonitor resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_InternetMonitor.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::InternetMonitor](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_InternetMonitor.html).

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
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnMonitor(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_internetmonitor.CfnMonitor",
):
    '''A CloudFormation ``AWS::InternetMonitor::Monitor``.

    The ``AWS::InternetMonitor::Monitor`` resource contains information about how you create a monitor in Amazon CloudWatch Internet Monitor. A monitor in Internet Monitor provides visibility into performance and availability between your applications hosted on AWS and your end users, using a traffic profile that it creates based on the application resources that you add: Virtual Private Clouds (VPCs), Amazon CloudFront distributions, or WorkSpaces directories.

    Internet Monitor also alerts you to internet issues that impact your application in the city-networks (locations and ASNs, typically internet service providers or ISPs) where your end users use it. With Internet Monitor, you can quickly pinpoint the locations and ASNs that are affected, so that you can address the issue.

    For more information, see `Using Amazon CloudWatch Internet Monitor <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html>`_ in the *Amazon CloudWatch User Guide* .

    :cloudformationResource: AWS::InternetMonitor::Monitor
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_internetmonitor as internetmonitor
        
        cfn_monitor = internetmonitor.CfnMonitor(self, "MyCfnMonitor",
            monitor_name="monitorName",
        
            # the properties below are optional
            max_city_networks_to_monitor=123,
            resources=["resources"],
            resources_to_add=["resourcesToAdd"],
            resources_to_remove=["resourcesToRemove"],
            status="status",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        monitor_name: builtins.str,
        max_city_networks_to_monitor: typing.Optional[jsii.Number] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        resources_to_add: typing.Optional[typing.Sequence[builtins.str]] = None,
        resources_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::InternetMonitor::Monitor``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param monitor_name: The name of the monitor. A monitor name can contain only alphanumeric characters, dashes (-), periods (.), and underscores (_).
        :param max_city_networks_to_monitor: The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the ASN, typically an internet service provider, that clients access the resources through. The city-network maximum that you choose sets a cap on the total that *can* be included when Internet Monitor monitors traffic with your monitor. You only pay for the number of city-networks that are actually monitored, not this maximum limit, and you can change the maximum at any time, by updating your monitor. For more information, see `Choosing a city-network maximum value <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html>`_ in *Using Amazon CloudWatch Internet Monitor* .
        :param resources: The resources that have been added for the monitor, listed by their Amazon Resource Names (ARNs).
        :param resources_to_add: The resources to add to a monitor, which you provide as a set of Amazon Resource Names (ARNs). You can add a combination of Virtual Private Clouds (VPCs) and Amazon CloudFront distributions, or you can add WorkSpaces directories. You can't add all three types of resources. .. epigraph:: If you add only VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.
        :param resources_to_remove: The resources to remove from a monitor. Provide the resources as a set of Amazon Resource Names (ARNs).
        :param status: The status of a monitor. The accepted values that you can specify for ``Status`` are ``ACTIVE`` and ``INACTIVE`` .
        :param tags: The tags for a monitor, listed as a set of *key:value* pairs.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b49625d902a7236b204a8a96b68b35647ded5da14fa0241503fe8aed7ec47718)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMonitorProps(
            monitor_name=monitor_name,
            max_city_networks_to_monitor=max_city_networks_to_monitor,
            resources=resources,
            resources_to_add=resources_to_add,
            resources_to_remove=resources_to_remove,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b595277fbc445515d03337a4dad34db4660278ac9bbe6f5c8b9c7ed6952d46)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c84a3dbe4ef362dc6094809148408f29e223dcdc3bde69c3aa5c6af04a3682bf)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time when the monitor was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''The last time that the monitor was modified.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrMonitorArn")
    def attr_monitor_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the monitor.

        :cloudformationAttribute: MonitorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMonitorArn"))

    @builtins.property
    @jsii.member(jsii_name="attrProcessingStatus")
    def attr_processing_status(self) -> builtins.str:
        '''The health of data processing for the monitor.

        For more information, see ``ProcessingStatus`` under `MonitorListMember <https://docs.aws.amazon.com/internet-monitor/latest/api/API_MonitorListMember.html>`_ in the *Amazon CloudWatch Internet Monitor API Reference* .

        :cloudformationAttribute: ProcessingStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProcessingStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrProcessingStatusInfo")
    def attr_processing_status_info(self) -> builtins.str:
        '''Additional information about the health of the data processing for the monitor.

        :cloudformationAttribute: ProcessingStatusInfo
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProcessingStatusInfo"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The tags for a monitor, listed as a set of *key:value* pairs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="monitorName")
    def monitor_name(self) -> builtins.str:
        '''The name of the monitor.

        A monitor name can contain only alphanumeric characters, dashes (-), periods (.), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-monitorname
        '''
        return typing.cast(builtins.str, jsii.get(self, "monitorName"))

    @monitor_name.setter
    def monitor_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef54ce1b63c1e0317ca73d33869cf2089b1ed66ab1da2e0c8fe45043287b6817)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitorName", value)

    @builtins.property
    @jsii.member(jsii_name="maxCityNetworksToMonitor")
    def max_city_networks_to_monitor(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of city-networks to monitor for your resources.

        A city-network is the location (city) where clients access your application resources from and the ASN, typically an internet service provider, that clients access the resources through.

        The city-network maximum that you choose sets a cap on the total that *can* be included when Internet Monitor monitors traffic with your monitor. You only pay for the number of city-networks that are actually monitored, not this maximum limit, and you can change the maximum at any time, by updating your monitor.

        For more information, see `Choosing a city-network maximum value <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html>`_ in *Using Amazon CloudWatch Internet Monitor* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-maxcitynetworkstomonitor
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCityNetworksToMonitor"))

    @max_city_networks_to_monitor.setter
    def max_city_networks_to_monitor(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44b26920fe092fdfabe5783619b4c150b5a44928ea63b71966ac31bfc9220c93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCityNetworksToMonitor", value)

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The resources that have been added for the monitor, listed by their Amazon Resource Names (ARNs).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-resources
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b341be6dedc5e43e3921317eb724e72355e140557e075d7a60632555b8e832c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @builtins.property
    @jsii.member(jsii_name="resourcesToAdd")
    def resources_to_add(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The resources to add to a monitor, which you provide as a set of Amazon Resource Names (ARNs).

        You can add a combination of Virtual Private Clouds (VPCs) and Amazon CloudFront distributions, or you can add WorkSpaces directories. You can't add all three types of resources.
        .. epigraph::

           If you add only VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-resourcestoadd
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcesToAdd"))

    @resources_to_add.setter
    def resources_to_add(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6eb4096ee765fe908d059e9b8acdca0ec1f047ddb2fe5ede304ab5ee82444f95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcesToAdd", value)

    @builtins.property
    @jsii.member(jsii_name="resourcesToRemove")
    def resources_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The resources to remove from a monitor.

        Provide the resources as a set of Amazon Resource Names (ARNs).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-resourcestoremove
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcesToRemove"))

    @resources_to_remove.setter
    def resources_to_remove(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9387e3cfcac600ed38b66e78df668311b567c717d8143713922de9b400262882)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcesToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of a monitor.

        The accepted values that you can specify for ``Status`` are ``ACTIVE`` and ``INACTIVE`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f131dc53d07b00ba7900326b379a6d12c142d61ae7d7045e4e4abbd87c853da1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_internetmonitor.CfnMonitorProps",
    jsii_struct_bases=[],
    name_mapping={
        "monitor_name": "monitorName",
        "max_city_networks_to_monitor": "maxCityNetworksToMonitor",
        "resources": "resources",
        "resources_to_add": "resourcesToAdd",
        "resources_to_remove": "resourcesToRemove",
        "status": "status",
        "tags": "tags",
    },
)
class CfnMonitorProps:
    def __init__(
        self,
        *,
        monitor_name: builtins.str,
        max_city_networks_to_monitor: typing.Optional[jsii.Number] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        resources_to_add: typing.Optional[typing.Sequence[builtins.str]] = None,
        resources_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMonitor``.

        :param monitor_name: The name of the monitor. A monitor name can contain only alphanumeric characters, dashes (-), periods (.), and underscores (_).
        :param max_city_networks_to_monitor: The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the ASN, typically an internet service provider, that clients access the resources through. The city-network maximum that you choose sets a cap on the total that *can* be included when Internet Monitor monitors traffic with your monitor. You only pay for the number of city-networks that are actually monitored, not this maximum limit, and you can change the maximum at any time, by updating your monitor. For more information, see `Choosing a city-network maximum value <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html>`_ in *Using Amazon CloudWatch Internet Monitor* .
        :param resources: The resources that have been added for the monitor, listed by their Amazon Resource Names (ARNs).
        :param resources_to_add: The resources to add to a monitor, which you provide as a set of Amazon Resource Names (ARNs). You can add a combination of Virtual Private Clouds (VPCs) and Amazon CloudFront distributions, or you can add WorkSpaces directories. You can't add all three types of resources. .. epigraph:: If you add only VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.
        :param resources_to_remove: The resources to remove from a monitor. Provide the resources as a set of Amazon Resource Names (ARNs).
        :param status: The status of a monitor. The accepted values that you can specify for ``Status`` are ``ACTIVE`` and ``INACTIVE`` .
        :param tags: The tags for a monitor, listed as a set of *key:value* pairs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_internetmonitor as internetmonitor
            
            cfn_monitor_props = internetmonitor.CfnMonitorProps(
                monitor_name="monitorName",
            
                # the properties below are optional
                max_city_networks_to_monitor=123,
                resources=["resources"],
                resources_to_add=["resourcesToAdd"],
                resources_to_remove=["resourcesToRemove"],
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a592873878a3205128bdbf7757cbce3b6e97783b1a68d0a1b5510ffc9f9f1fd8)
            check_type(argname="argument monitor_name", value=monitor_name, expected_type=type_hints["monitor_name"])
            check_type(argname="argument max_city_networks_to_monitor", value=max_city_networks_to_monitor, expected_type=type_hints["max_city_networks_to_monitor"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument resources_to_add", value=resources_to_add, expected_type=type_hints["resources_to_add"])
            check_type(argname="argument resources_to_remove", value=resources_to_remove, expected_type=type_hints["resources_to_remove"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "monitor_name": monitor_name,
        }
        if max_city_networks_to_monitor is not None:
            self._values["max_city_networks_to_monitor"] = max_city_networks_to_monitor
        if resources is not None:
            self._values["resources"] = resources
        if resources_to_add is not None:
            self._values["resources_to_add"] = resources_to_add
        if resources_to_remove is not None:
            self._values["resources_to_remove"] = resources_to_remove
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def monitor_name(self) -> builtins.str:
        '''The name of the monitor.

        A monitor name can contain only alphanumeric characters, dashes (-), periods (.), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-monitorname
        '''
        result = self._values.get("monitor_name")
        assert result is not None, "Required property 'monitor_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_city_networks_to_monitor(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of city-networks to monitor for your resources.

        A city-network is the location (city) where clients access your application resources from and the ASN, typically an internet service provider, that clients access the resources through.

        The city-network maximum that you choose sets a cap on the total that *can* be included when Internet Monitor monitors traffic with your monitor. You only pay for the number of city-networks that are actually monitored, not this maximum limit, and you can change the maximum at any time, by updating your monitor.

        For more information, see `Choosing a city-network maximum value <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html>`_ in *Using Amazon CloudWatch Internet Monitor* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-maxcitynetworkstomonitor
        '''
        result = self._values.get("max_city_networks_to_monitor")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The resources that have been added for the monitor, listed by their Amazon Resource Names (ARNs).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def resources_to_add(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The resources to add to a monitor, which you provide as a set of Amazon Resource Names (ARNs).

        You can add a combination of Virtual Private Clouds (VPCs) and Amazon CloudFront distributions, or you can add WorkSpaces directories. You can't add all three types of resources.
        .. epigraph::

           If you add only VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-resourcestoadd
        '''
        result = self._values.get("resources_to_add")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def resources_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The resources to remove from a monitor.

        Provide the resources as a set of Amazon Resource Names (ARNs).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-resourcestoremove
        '''
        result = self._values.get("resources_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of a monitor.

        The accepted values that you can specify for ``Status`` are ``ACTIVE`` and ``INACTIVE`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for a monitor, listed as a set of *key:value* pairs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMonitorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMonitor",
    "CfnMonitorProps",
]

publication.publish()

def _typecheckingstub__b49625d902a7236b204a8a96b68b35647ded5da14fa0241503fe8aed7ec47718(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    monitor_name: builtins.str,
    max_city_networks_to_monitor: typing.Optional[jsii.Number] = None,
    resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    resources_to_add: typing.Optional[typing.Sequence[builtins.str]] = None,
    resources_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b595277fbc445515d03337a4dad34db4660278ac9bbe6f5c8b9c7ed6952d46(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c84a3dbe4ef362dc6094809148408f29e223dcdc3bde69c3aa5c6af04a3682bf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef54ce1b63c1e0317ca73d33869cf2089b1ed66ab1da2e0c8fe45043287b6817(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b26920fe092fdfabe5783619b4c150b5a44928ea63b71966ac31bfc9220c93(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b341be6dedc5e43e3921317eb724e72355e140557e075d7a60632555b8e832c4(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eb4096ee765fe908d059e9b8acdca0ec1f047ddb2fe5ede304ab5ee82444f95(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9387e3cfcac600ed38b66e78df668311b567c717d8143713922de9b400262882(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f131dc53d07b00ba7900326b379a6d12c142d61ae7d7045e4e4abbd87c853da1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a592873878a3205128bdbf7757cbce3b6e97783b1a68d0a1b5510ffc9f9f1fd8(
    *,
    monitor_name: builtins.str,
    max_city_networks_to_monitor: typing.Optional[jsii.Number] = None,
    resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    resources_to_add: typing.Optional[typing.Sequence[builtins.str]] = None,
    resources_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
