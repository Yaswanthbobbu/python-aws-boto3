import boto3

s3 = boto3.client('s3')

def create_bucket(bucket_name, region=None):
    if region is None or region == 'us-east-1':
        response = s3.create_bucket(
            Bucket=bucket_name,
            ACL="private"
        )
    else:
        response = s3.create_bucket(
            Bucket=bucket_name,
            ACL="private",
            CreateBucketConfiguration={'LocationConstraint': region}
        )
    print(response)

create_bucket('boto3-bucket2-02062025')

