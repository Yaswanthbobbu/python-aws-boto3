import boto3


def delete_bucket_policy(bucket_name):
    s3 = boto3.client('s3')

    try:
        s3.delete_bucket_policy(Bucket=bucket_name)
        print(f"Bucket policy deleted for bucket: {bucket_name}")
    except Exception as e:
        print(f"Error deleting bucket policy for {bucket_name}: {e}")

delete_bucket_policy('boto3-bucket-02062025')