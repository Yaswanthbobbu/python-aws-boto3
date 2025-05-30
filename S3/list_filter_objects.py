import boto3

s3_resource = boto3.resource('s3', 'us-east-1')

def list_filter(bucket_name):
    s3_bucket = s3_resource.Bucket(bucket_name)
    for obj in s3_bucket.objects.filter(Prefix='test'):
        print(obj.key)

list_filter('sample-boto3-bucket-python')
