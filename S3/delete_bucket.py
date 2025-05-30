import boto3

"""
bucket = boto3.client('s3', region_name='us-east-1')

def delete_bucket(bucket_name):
    response = bucket.delete_bucket(Bucket=bucket_name)
    print(response)

delete_bucket('sample-boto3-bucket-python')

"""

bucket = boto3.resource('s3', 'us-east-1')

def delete_bucket(bucket_name):
    response = bucket.Bucket(bucket_name)
    response.delete()
    return

delete_bucket('sample-boto3-bucket-python')

##