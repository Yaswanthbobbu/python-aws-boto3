import boto3

s3_resource = boto3.resource('s3', 'us-east-1')

def list_file(bucket_name):
    s3_bucket = s3_resource.Bucket(bucket_name)
    for obj in s3_bucket.objects.all():
        print(obj.key)

list_file('sample-boto3-bucket-python')

