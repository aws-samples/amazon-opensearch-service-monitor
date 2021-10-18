'''
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
'''

from collections import namedtuple
from datetime import datetime, timedelta
from dateutil import tz, parser
import itertools
import json
import os
import time
import uuid


import boto3
from es_sink.descriptor import ESDescriptor, IndexDescriptor
import es_sink.es_auth
from es_sink.es_transport import ESTransport
import es_sink.flushing_buffer

# Lambda Interval Settings (seconds)
LAMBDA_INTERVAL=300

# This structure details the metrics available per domain. Domain names are unique
# by region, but not globally, so the identifier includes the domain name and region
# pair. The metric_descriptions are a collection of SingleMetricDescriptions, which
# provide the dimensions to pass to CloudWatch to retrieve the values for the 
# metric.
DomainMetricsAvailable = namedtuple('DomainMetricsAvailable', 
                                    ('region', 'domain_name', 'metric_descriptions'))
SingleMetricDescription = namedtuple('SingleMetricDescription', 
                                     ('metric_name', 'dims'))


SingleMetricValue = namedtuple('SingleMetricValue',
                               ('region', 'domain_name', 'metric_name', 'stat', 
                                'value', 'timestamp'))


################################################################################
# Environment
DDB_TABLE = os.environ['TABLE']

DOMAIN_ENDPOINT = os.environ['DOMAIN_ENDPOINT']
DOMAIN_ADMIN_UNAME = os.environ['DOMAIN_ADMIN_UNAME']
DOMAIN_ADMIN_PW = os.environ['DOMAIN_ADMIN_PW']
REGIONS = json.loads(os.environ['REGIONS'])

################################################################################
# Timestamp tracking

def get_last_timestamp_ddb(domain_name, region):
    ddb = boto3.client('dynamodb')
    try:
        ret = ddb.get_item(TableName=DDB_TABLE,
                            Key={'domain': {'S': domain_name},
                                 'region': {'S': region}})
        if not ret or not ret.get('Item', None):
            return None
        iso_ts = ret['Item'].get('Timestamp', None)
        if not iso_ts:
            return None
        iso_ts = iso_ts['S']
        return parser.parse(iso_ts)
    except Exception as e:
        print('Exception retrieving timestamp for "{}:{}"'.format(domain_name, region))
        print(e)
    return None


def update_metric_timestamp_ddb(domain_name, region, ts):
    ddb = boto3.client('dynamodb')
    try:
        existing = get_last_timestamp_ddb(domain_name, region)
        if not existing or (existing and existing < ts):
            ddb.update_item(
                TableName=DDB_TABLE,
                Key={ 'domain': {'S': domain_name},
                      'region': {'S': region}},
                AttributeUpdates={'Timestamp': { 'Value': {'S': ts.isoformat()}}}
            )
    except Exception as e:
        print('Exception putting timestamp for "{}:{}"'.format(domain_name, region))
        print(e)


LAST_TIMESTAMPS = dict()
def update_metric_timestamp(domain_name, region, ts):
    tup = (domain_name, region)
    existing = LAST_TIMESTAMPS.get(tup, None)
    if existing and existing < ts:
        LAST_TIMESTAMPS[tup] = ts
    elif not existing:
        LAST_TIMESTAMPS[tup] = ts
    # otherwise, there's a newer timestamp so don't change anything


def get_last_timestamp(domain_name, region):
    return LAST_TIMESTAMPS.get((domain_name, region))
################################################################################


################################################################################
# Domain tracking; 

def list_all_domains():
    ''' Loops through the list of REGIONS, listing out all domains for this
        account in that region. Returns a list of domain names. 
    '''
    doms = {}
    for region in REGIONS:
        es = boto3.client('es', region)
        try:
            resp = es.list_domain_names()
            resp = resp['DomainNames']
            doms[region] = [val['DomainName'] for val in resp]
        except Exception as e:
            print('Failed to get domain names in region: {}'.format(region))
            print(e)
    return doms


################################################################################
# CloudWatch interface
# 
def list_domain_cloudwatch_metrics(domain_name=None, region=None):
    ''' For a particular domain/region, list all available metrics. Different
        ES versions have different metrics for them. This ensures retrieving
        all metrics.
        Returns a list of SingleMetricDescriptions
    '''
    cw = boto3.client('cloudwatch', region)
    paginator = cw.get_paginator('list_metrics')
    iter = paginator.paginate(
        Dimensions=[
            {
                'Name': 'DomainName',
                'Value': domain_name
            }
        ]
    )
    resp = []
    for page in iter:
        metrics = page['Metrics']
        for metric in metrics:
            resp.append(SingleMetricDescription(metric_name=metric['MetricName'], 
                                                dims=metric['Dimensions']))
    return resp


def get_all_domain_metric_descriptions(doms):
    ''' Takes a list of dicts - region: list of domains and retrieves the available
        metrics for each of the domains.
    '''
    resp = []
    for region, domains in doms.items():
        for domain in domains:
            dmets = list_domain_cloudwatch_metrics(domain_name=domain,
                                                   region=region)
            resp.append(DomainMetricsAvailable(region, domain, dmets))
    return resp


def build_metric_data_queries(domain_name, region, metric_descriptions):
    ret = []
    for md in metric_descriptions:
        metric_name = md.metric_name
        for stat in ['Minimum', 'Maximum', 'Average']: # What flexibility does this need?
            label = '{} {} {} {}'.format(domain_name, region, metric_name, stat)
            _id = 'a' + str(uuid.uuid1()).lower().replace('-', '_')
            ret.append(
                    {
                        'Id': _id,
                        'Label': label,
                        'MetricStat': {
                            'Metric': {
                                'Namespace': 'AWS/ES',
                                'MetricName': metric_name,
                                'Dimensions': md.dims
                            },
                            'Period': LAMBDA_INTERVAL, # ? any need to do more granular than 1 minute?
                            'Stat': stat,
                        }
                    }
            )
    return ret


def grouper(iterable, n):
    it = iter(iterable)
    while True:
       chunk = list(itertools.islice(it, n))
       if not chunk:
           return
       yield chunk


def get_single_domain_metric_values(domain_name, region, metric_descriptions):
    # TODO: Make this multi-domain?
    ret = list()
    cw = boto3.client('cloudwatch', region)
    queries = build_metric_data_queries(domain_name, region, metric_descriptions)

    # The CW query runs from now to the last time this retrieved data. It could miss
    # data points on edge case boundaries.
    time_now = datetime.utcfromtimestamp(time.time())
    last_timestamp = get_last_timestamp_ddb(domain_name, region)
    if not last_timestamp:
        last_timestamp = time_now - timedelta(minutes=15)

    for group in grouper(queries, 100):
        try:
            paginator = cw.get_paginator('get_metric_data')
            iter = paginator.paginate(MetricDataQueries=group,
                                      StartTime=last_timestamp,
                                      EndTime=time_now)
            for page in iter:
                for result in page['MetricDataResults']:
                    # TODO: Error handling
                    (result_domain, result_region, metric_name, stat) = result['Label'].split(' ')
                    for val in zip(result['Timestamps'], result['Values']):
                        ts = val[0].replace(microsecond=0, tzinfo=tz.tzutc())
                        ret.append(SingleMetricValue(
                            domain_name=result_domain,
                            region=result_region,
                            metric_name=metric_name,
                            stat=stat,
                            timestamp=ts.isoformat(),
                            value=val[1]
                        ))
            update_metric_timestamp_ddb(domain_name, region, time_now)
        except Exception as e:
            # Handle me better
            print('Exception', domain_name, region)
            print(e)
            print()
    return ret


def get_all_domain_metric_values(domains):
    ''' Domains is a list of DomainMetricDescriptions - tuples with domain_name,
        region, and a list of SingleMetricDescriptions.
        Returns a list of SingleMetricValues.
    '''
    # TODO: Send a single request rather than 1 per domain/region dimension
    res = list()
    for domain in domains:
        domain_name = domain.domain_name
        region = domain.region
        res.extend(get_single_domain_metric_values(domain_name, region, domain.metric_descriptions))
    return res


################################################################################
# Amazon OpenSearch interface

INDEX_DESCRIPTOR = IndexDescriptor(es_index='domains', es_v7=True, timestamped=True)
ES_AUTH = es_sink.es_auth.ESHttpAuth(DOMAIN_ADMIN_UNAME, DOMAIN_ADMIN_PW)
ES_DESCRIPTOR = ESDescriptor(
    endpoint=DOMAIN_ENDPOINT,
    index_descriptor=INDEX_DESCRIPTOR,
    auth=ES_AUTH
)
ES_BUFFER = es_sink.flushing_buffer.flushing_buffer_factory(ES_DESCRIPTOR,
                                                            flush_trigger=1000)


def send_all_domain_metric_values(values):
    total = 0
    total_flushed = 0
    for value in values:

        d = value._asdict()
        line_value = d.pop('value')
        metric_name = d['metric_name']
        d[metric_name] = line_value

        # Rename field timestamp to @timestamp
        timestamp_value = d.pop('timestamp')
        d['@timestamp'] = timestamp_value

        log_line = json.dumps(d)

        f, ignore = ES_BUFFER.add_log_line(log_line)

        total_flushed += f
        total += 1

    print('Added {} log lines to the buffer'.format(total))
    print('Flushed {} log lines'.format(total_flushed))


################################################################################
# Lambda handler
def handler(event, context):
    doms = list_all_domains()
    all_mets = get_all_domain_metric_descriptions(doms)
    vals = get_all_domain_metric_values(all_mets)
    send_all_domain_metric_values(vals)
    ES_BUFFER.flush()


################################################################################
# Command line/test interface
if __name__ == '__main__':
    # This code will normally run as a lambda function, so I don't want to add a
    # command-line arg. Instead, set an environment variable as if it were 
    # running as lambda.
    print()
    print('Did you remember to set the "TABLE" environment variable with the')
    print('name of the DDB table tracking timestamps?')
    print('Did you remember to set the "DOMAIN_ENDPOINT", DOMAIN_ADMIN_UNAME, and')
    print('DOMAIN_UNAME_PW environment variables?')
    print()

    doms = list_all_domains()
    print_doms(doms)

    print('Getting all metric descriptions')
    all_mets = get_all_domain_metric_descriptions(doms)
    print_all_mets(all_mets)

    while 1:
        print('Retrieving metric values')
        vals = get_all_domain_metric_values(all_mets)
        print_all_vals(vals)
        print('Adding new metric values')
        send_all_domain_metric_values(vals)
        ES_BUFFER.flush()


def print_doms(doms):
    print("Monitoring domains:")
    for region, domains in doms.items():
        print(region)
        for domain in domains:
            print('\t' + domain)


def print_all_mets(all_mets):
    for met in all_mets:
        print('\t{}/{}: {} metrics'.format(met.domain_name, met.region,
                                           len(met.metric_descriptions)))
def print_all_vals(vals):
    doms = dict()
    for val in vals:
        if not (val.domain_name, val.region) in doms.keys():
            doms[(val.domain_name, val.region)] = 0
        doms[(val.domain_name, val.region)] += 1
    print('Retrieved {} values'.format(len(vals)))
    total = 0
    for dom, count in doms.items():
        print('{}: {}'.format(dom, count))
        total += count
    print('Retrieved a total of {} values'.format(total))
