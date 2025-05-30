import boto3

bucket = boto3.resource('s3', region_name='us-east-1')

def create_bucket(bucket_name):
    response = bucket.create_bucket(
        Bucket=bucket_name,
        ACL="private"  
    )
    print(response)

create_bucket("boto3-bucket")

##