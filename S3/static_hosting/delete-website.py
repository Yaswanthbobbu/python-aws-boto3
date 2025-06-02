import boto3

def delete_website_configuration(bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.delete_bucket_website(Bucket=bucket_name)
        print(f"Static website configuration deleted for bucket: {bucket_name}")
    except s3.exceptions.NoSuchWebsiteConfiguration:
        print(f"No static website configuration found for bucket: {bucket_name}")
    except Exception as e:
        print(f"Error deleting website configuration for {bucket_name}: {e}")


delete_website_configuration('boto3-bucket-02062025')