import boto3


bucket = boto3.client('s3', region_name='us-east-1')

def list_bucket():
    response = bucket.list_buckets()
    for item in response['Buckets']:
        print(item)
"""

s3_resource = boto3.resource('s3', region_name='us-east-1')

def list_bucket():
    all_buckets = s3_resource.buckets.all()
    for item in all_buckets:
        print(item.name)
        
"""

list_bucket()