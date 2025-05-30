import boto3

s3_resource = boto3.resource('s3', 'us-east-1')

def download_file(file_name, bucket_name):
    s3_bucket = s3_resource.Object(bucket_name, file_name)
    s3_bucket.download_file('download.txt')

download_file('file.txt', 'sample-boto3-bucket-python')

