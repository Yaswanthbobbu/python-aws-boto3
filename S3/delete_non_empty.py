import boto3

bucket = boto3.resource('s3', region_name='us-east-1')

def clean_up(bucket_name):
    s3_bucket = bucket.Bucket(bucket_name)
    for obj in s3_bucket.objects.all():
        obj.delete()

    for obj_ver in s3_bucket.object_versions.all():
        obj_ver.delete()

clean_up('sample-boto3-bucket-python')

bucket.delete('sample-boto3-bucket-python')

