'''
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
'''

#!/usr/bin/env python3

from aws_cdk import core

from monitoring_cdk.monitoring_cdk_stack import MonitoringCdkStack


app = core.App()
MonitoringCdkStack(app, "monitoring-cdk")

app.synth()
