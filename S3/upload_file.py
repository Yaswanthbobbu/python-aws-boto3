import boto3

"""
bucket = boto3.client('s3', 'us-east-1')

def upload_file(file_name, bucket_name, obj_name=None, args=None):
    if obj_name is None:
        obj_name = file_name

    bucket.upload_file(file_name, bucket_name, obj_name, ExtraArgs=args)
    print(f"{file_name} has been uploaded to {bucket_name}")

upload_file('file.txt','sample-boto3-bucket-python')

"""

bucket = boto3.resource('s3', 'us-east-1')

def upload_files(file_name, bucket_name, obj_name=None, args=None):
    if obj_name is None:
        obj_name = file_name

    bucket.meta.client.upload_file(file_name, bucket_name, obj_name, ExtraArgs=args)
    print(f"{file_name} has been uploaded to {bucket_name}")

upload_files('file2.txt', 'sample-boto3-bucket-python')

