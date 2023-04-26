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
import requests
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
from requests_aws4auth import AWS4Auth
from datetime import datetime
import boto3


# Lambda Interval Settings (seconds)
LAMBDA_INTERVAL=60

################################################################################
# Environment

DOMAIN_ENDPOINT = os.environ['DOMAIN_ENDPOINT'].replace('https://','')
DOMAIN_ADMIN_UNAME = os.environ['DOMAIN_ADMIN_UNAME']
DOMAIN_ADMIN_PW = os.environ['DOMAIN_ADMIN_PW']
REGIONS = json.loads(os.environ['REGIONS'])
SERVERLESS_REGIONS = json.loads(os.environ['SERVERLESS_REGIONS'])
current_date_time = (datetime.now()).isoformat()
today_ = datetime.today().strftime('%Y-%m-%d')

#Creating session Object

session=boto3.Session(
        
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        aws_session_token=os.environ['AWS_SESSION_TOKEN']
    )


# Amazon OpenSearch interface
                                                                      
AOS_client_ = OpenSearch(
            [
                'https://'+DOMAIN_ADMIN_UNAME+':'+DOMAIN_ADMIN_PW+'@'+DOMAIN_ENDPOINT+':443/'
            ],
            verify_certs=True
        )
        

def list_all_domains():
    ''' Loops through the list of REGIONS, listing out all domains for this
        account in that region. Returns a list of domain names.
    '''
    print("Started processing for list_all_domains")
    
    list_domains = []
    
    for region in REGIONS:
        es = boto3.client('opensearch', region)
        resp = es.list_domain_names()
        list_domains.append(resp['DomainNames'])
    
    return list_domains
            
            
            
def send_all_domain_config_values(values):
    doms_config = []
    
    
    for domain in values[0]:
        
        es = boto3.client('opensearch')
        temp_ = es.describe_domain(
                DomainName=domain['DomainName'])['DomainStatus']
        temp_['ServiceSoftwareOptions'].pop('AutomatedUpdateDate')
        doms_config.append(temp_)
                
    
    action = json.dumps({ "index": { "_index": "domain_configuration-"+today_} })
    
    body_ =""
    
    for domain_ in doms_config:
        domain_['@timestamp'] = current_date_time
        domain_['native_domain'] = domain_['DomainName']
        body_ += action+"\n"+json.dumps(domain_)+"\n" 
        
    
    AOS_client_.indices.delete('domain_configuration*')
    AOS_client_.indices.create("domain_configuration-"+today_,body={
  "mappings" : {
      "properties" : {
        "@timestamp" : {
          "type" : "date"
        },
        "ARN" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "AccessPolicies" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "AdvancedOptions" : {
          "properties" : {
            "indices" : {
              "properties" : {
                "fielddata" : {
                  "properties" : {
                    "cache" : {
                      "properties" : {
                        "size" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "query" : {
                  "properties" : {
                    "bool" : {
                      "properties" : {
                        "max_clause_count" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            },
            "override_main_response_version" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "rest" : {
              "properties" : {
                "action" : {
                  "properties" : {
                    "multi" : {
                      "properties" : {
                        "allow_explicit_index" : {
                          "type" : "text",
                          "fields" : {
                            "keyword" : {
                              "type" : "keyword",
                              "ignore_above" : 256
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "AdvancedSecurityOptions" : {
          "properties" : {
            "AnonymousAuthEnabled" : {
              "type" : "boolean"
            },
            "Enabled" : {
              "type" : "boolean"
            },
            "InternalUserDatabaseEnabled" : {
              "type" : "boolean"
            }
          }
        },
        "AutoTuneOptions" : {
          "properties" : {
            "State" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "UseOffPeakWindow" : {
              "type" : "boolean"
            }
          }
        },
        "ClusterConfig" : {
          "properties" : {
            "ColdStorageOptions" : {
              "properties" : {
                "Enabled" : {
                  "type" : "boolean"
                }
              }
            },
            "DedicatedMasterCount" : {
              "type" : "integer"
            },
            "DedicatedMasterEnabled" : {
              "type" : "boolean"
            },
            "DedicatedMasterType" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "InstanceCount" : {
              "type" : "long"
            },
            "InstanceType" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "WarmEnabled" : {
              "type" : "boolean"
            },
            "ZoneAwarenessConfig" : {
              "properties" : {
                "AvailabilityZoneCount" : {
                  "type" : "long"
                }
              }
            },
            "ZoneAwarenessEnabled" : {
              "type" : "boolean"
            }
          }
        },
        "CognitoOptions" : {
          "properties" : {
            "Enabled" : {
              "type" : "boolean"
            }
          }
        },
        "Created" : {
          "type" : "boolean"
        },
        "Deleted" : {
          "type" : "boolean"
        },
        "DomainEndpointOptions" : {
          "properties" : {
            "CustomEndpointEnabled" : {
              "type" : "boolean"
            },
            "EnforceHTTPS" : {
              "type" : "boolean"
            },
            "TLSSecurityPolicy" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            }
          }
        },
        "DomainId" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "DomainName" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "EBSOptions" : {
          "properties" : {
            "EBSEnabled" : {
              "type" : "boolean"
            },
            "Iops" : {
              "type" : "long"
            },
            "Throughput" : {
              "type" : "long"
            },
            "VolumeSize" : {
              "type" : "long"
            },
            "VolumeType" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            }
          }
        },
        "EncryptionAtRestOptions" : {
          "properties" : {
            "Enabled" : {
              "type" : "boolean"
            },
            "KmsKeyId" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            }
          }
        },
        "Endpoint" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "Endpoints" : {
          "properties" : {
            "vpc" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            }
          }
        },
        "EngineVersion" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "NodeToNodeEncryptionOptions" : {
          "properties" : {
            "Enabled" : {
              "type" : "boolean"
            }
          }
        },
        "OffPeakWindowOptions" : {
          "properties" : {
            "Enabled" : {
              "type" : "boolean"
            },
            "OffPeakWindow" : {
              "properties" : {
                "WindowStartTime" : {
                  "properties" : {
                    "Hours" : {
                      "type" : "long"
                    },
                    "Minutes" : {
                      "type" : "long"
                    }
                  }
                }
              }
            }
          }
        },
        "Processing" : {
          "type" : "boolean"
        },
        "ServiceSoftwareOptions" : {
          "properties" : {
            "Cancellable" : {
              "type" : "boolean"
            },
            "CurrentVersion" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "Description" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "NewVersion" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "OptionalDeployment" : {
              "type" : "boolean"
            },
            "UpdateAvailable" : {
              "type" : "boolean"
            },
            "UpdateStatus" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            }
          }
        },
        "SnapshotOptions" : {
          "properties" : {
            "AutomatedSnapshotStartHour" : {
              "type" : "long"
            }
          }
        },
        "SoftwareUpdateOptions" : {
          "properties" : {
            "AutoSoftwareUpdateEnabled" : {
              "type" : "boolean"
            }
          }
        },
        "UpgradeProcessing" : {
          "type" : "boolean"
        },
        "VPCOptions" : {
          "properties" : {
            "AvailabilityZones" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "SecurityGroupIds" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "SubnetIds" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "VPCId" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            }
          }
        },
        "native_domain" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        }
      }
    }
})
    response = AOS_client_.bulk(
                         index = 'domain_configuration',
                         body = body_)
    print(response)
    
    return doms_config
    
    
    # Curl <optional Code>    
    
    #url = DOMAIN_ENDPOINT+'/_bulk'
    #headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    #r = requests.post(url, data=body_, headers=headers, auth = (DOMAIN_ADMIN_UNAME,DOMAIN_ADMIN_PW))
    #print(r)
    
def send_all_domain_indices_shard_allocation_config_values(values,doms_config):

    credentials = session.get_credentials()
    region = 'us-east-1'
    service = 'execute-api'
    
    awsauth = AWSV4SignerAuth(credentials, region)
    
    headers = { "Content-Type": "application/json"}
    
    AOS_client_.indices.delete('domain_indices_configuration*')
    AOS_client_.indices.create('domain_indices_configuration-'+today_,body={"mappings" : {
      "properties" : {
        "@timestamp" : {
          "type" : "date"
        },
        "health" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "index_id" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "index_name" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "native_domain" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "num_docs" : {
          "type" : "long"
        },
        "num_docs_deleted" : {
          "type" : "long"
        },
        "primary_shards" : {
          "type" : "integer"
        },
        "primary_storage" : {
          "type" : "float"
        },
        "replication" : {
          "type" : "integer"
        
        },
        "shard_size" : {
          "type" : "float"
        },
        "status" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "total_storage" : {
          "type" : "float"
      
        }
      }
    }} )
    
   
    
    AOS_client_.indices.delete('domain_nodes_allocation*')
    AOS_client_.indices.create('domain_nodes_allocation-'+today_,body={ "mappings" : {
      "properties" : {
        "@timestamp" : {
          "type" : "date"
        },
        "EBSEnabled" : {
          "type" : "boolean"
        },
        "VolumeSize" : {
          "type" : "long"
        },
        "VolumeType" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "free_disk_space_available" : {
          "type" : "long"

        },
        "host" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "indices_disk_space_occupied" : {
          "type" : "float"
        },
        "ip" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "native_domain" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "node_id" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "node_type" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "number_of_shards" : {
          "type" : "integer"

        },
        "skew_in_percent" : {
          "type" : "float"
        },
        "total_disk_space" : {
          "type" : "long"

        },
        "total_disk_space_occupied" : {
          "type" : "long"
      
        },
        "total_percentage_of_disk_space_in_use" : {
          "type" : "long"
        }
      }
    }})

    
    
    
    AOS_client_.indices.delete('domain_shards_config*')
    AOS_client_.indices.create('domain_shards_config-'+today_,body={"mappings" : {
      "properties" : {
        "@timestamp" : {
          "type" : "date"
        },
        "docs" : {
          "type" : "integer"

        },
        "index_name" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "ip" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "native_domain" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "node_id" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "node_type" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "primary_or_replica" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "shard_num_in_index" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "shard_size" : {
          "type" : "long"

        },
        "state" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        }
      }
    }})


    # Fetch _cat/indices from all domains and ingest into monitoring domain
    # One bulk api gets triggered for every domain
    # pre-requisite: The backend role (this lambda's execution role) should be configured in every candidate domain 
    
    
    for domain in doms_config:
        print(domain)
        
        if('Endpoint' in domain):
            endpoint = domain['Endpoint']
        else:
            endpoint = domain['Endpoints']['vpc']
        
        
        body_=''
        action = json.dumps({ "index": { "_index": "domain_indices_configuration-"+today_} })
        
        # Connect to the candidate domain
        
        client = OpenSearch(
        hosts = [{'host': endpoint, 'port': 443}],
        http_auth = awsauth,
        timeout=60,
        use_ssl = True,
        #verify_certs = True,
        connection_class = RequestsHttpConnection
        )
        
        response = client.cat.indices(bytes='b')[:-1]
        
        print('connection successful with '+ domain['DomainName'] + ' domain')
        
        indices = response.split('\n')
        indices_dic = {}
        
        # format the indices response into JSON docs
        
        for i in indices:
            arr = i.split()
            indices_dic['native_domain'] = domain['DomainName']
            indices_dic['health'] = arr[0]
            indices_dic['status'] = arr[1]
            indices_dic['index_name'] = arr[2]
            indices_dic['index_id'] = arr[3]
            indices_dic['primary_shards'] = arr[4]
            indices_dic['replication'] = arr[5]
            indices_dic['num_docs'] = arr[6]
            indices_dic['num_docs_deleted'] = arr[7]
            indices_dic['total_storage'] = arr[8]
            indices_dic['primary_storage'] = arr[9]
            indices_dic['shard_size'] = int(indices_dic['primary_storage'])/int(indices_dic['primary_shards'])
            indices_dic['@timestamp'] = current_date_time
            body_ += action+"\n"+json.dumps(indices_dic)+"\n" 
                    
    
        
        # Bulk insert into the monitoring domain
        
        response = AOS_client_.bulk(
                         index = 'domain_indices_configuration',
                         body = body_)
        
        print(response)
        
        # Fetch _cat/allocation from all domains and ingest into monitoring domain
        # One bulk api gets triggered for every domain
        # pre-requisite: The backend role (this lambda's execution role) should be configured in every candidate domain 
    
        response = client.cat.allocation(bytes='b')[:-1]
        allocation = response.split('\n')
        
        # format the allocation response into JSON docs
        
        allocation_dic = {}
        indices_disk_space_occupied = []
        bulk_body = []


        for i in allocation:
            arr = i.split()
            if len(arr)<9:
                continue
            allocation_dic = {}
            allocation_dic['native_domain'] = domain['DomainName']
            allocation_dic['number_of_shards'] = arr[0]
            allocation_dic['indices_disk_space_occupied'] = float(arr[1])
            indices_disk_space_occupied.append(float(arr[1]))
            allocation_dic['total_disk_space_occupied'] = arr[2]
            allocation_dic['free_disk_space_available'] = arr[3]
            allocation_dic['total_disk_space'] = arr[4]
            allocation_dic['total_percentage_of_disk_space_in_use'] = arr[5]
            allocation_dic['host'] = arr[6]
            allocation_dic['ip'] = arr[7]
            allocation_dic['node_id'] = arr[8]
            allocation_dic['node_type'] = domain['ClusterConfig']['InstanceType']
            allocation_dic['EBSEnabled'] = domain['EBSOptions']['EBSEnabled']
            allocation_dic['VolumeType'] = domain['EBSOptions']['VolumeType']
            allocation_dic['VolumeSize'] = domain['EBSOptions']['VolumeSize']
            allocation_dic['@timestamp'] = current_date_time
            bulk_body.append(allocation_dic)
        
        
        # Calculate the storage skew across nodes
        average_storage_occupied = sum(indices_disk_space_occupied)/len(indices_disk_space_occupied)
        
        action = json.dumps({ "index": { "_index": "domain_nodes_allocation-"+today_ } })
        body_=''
        
        for j in bulk_body:
            
            j['skew_in_percent'] = ((average_storage_occupied-j['indices_disk_space_occupied'])/average_storage_occupied)*100
            
            body_ += action+"\n"+json.dumps(j)+"\n" 

   
        response = AOS_client_.bulk(
                         index = 'domain_nodes_allocation',
                         body = body_)
        print(response)
        
        # Fetch _cat/shards from all domains and ingest into monitoring domain
        # One bulk api gets triggered for every domain
        # pre-requisite: The backend role (this lambda's execution role) should be configured in every candidate domain   
        
        
        response = client.cat.shards(bytes='b')[:-1]
        shards = response.split('\n')
        shards_dic = {}
        
        action = json.dumps({ "index": { "_index": "domain_shards_config-"+today_} })
        body_=''
        
        # format the shards response into JSON docs
        
        
        for i in shards:
            arr = i.split()
            if len(arr)<8:
                continue
            shards_dic['native_domain'] = domain['DomainName']
            shards_dic['index_name'] = arr[0]
            shards_dic['shard_num_in_index'] = arr[1]
            shards_dic['primary_or_replica'] = arr[2]
            shards_dic['state'] = arr[3]
            shards_dic['docs'] = arr[4]
            shards_dic['shard_size'] = arr[5]
            shards_dic['ip'] = arr[6]
            shards_dic['node_id'] = arr[7]
            shards_dic['node_type'] = domain['ClusterConfig']['InstanceType']
            if int(arr[5]) > 53687091200:
                shards_dic['is_large_shard'] = 1  
            else:
                shards_dic['is_large_shard'] = 0
            if int(arr[5]) < 10737418240:
                shards_dic['is_small_shard'] = 1  
            else:
                shards_dic['is_small_shard'] = 0
            if int(arr[5]) < 10737418240:
                shards_dic['is_small_shard'] = 1  
            else:
                shards_dic['is_small_shard'] = 0
            shards_dic['@timestamp'] = current_date_time

            
            body_ += action+"\n"+json.dumps(shards_dic)+"\n" 
        
        
        response = AOS_client_.bulk(
                         index = 'domain_shards_config',
                         body = body_)
        print(response)


# Lambda handler
def handler(event, context):
    doms = list_all_domains()
    dom_config = send_all_domain_config_values(doms)
    send_all_domain_indices_shard_allocation_config_values(doms,dom_config)

