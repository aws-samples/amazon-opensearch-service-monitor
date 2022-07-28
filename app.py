'''
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
'''

#!/usr/bin/env python3

from aws_cdk import App

from opensearch.opensearch_monitor_stack import OpenSearchMonitor


app = App()
OpenSearchMonitor(app, "opensearch-monitor-stack")

app.synth()
