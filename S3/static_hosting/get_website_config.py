import boto3
from pprint import pprint

def get_website_configuration(bucket_name):
    s3 = boto3.client('s3')

    try:
        response = s3.get_bucket_website(Bucket=bucket_name)
        pprint(response)
    except s3.exceptions.NoSuchWebsiteConfiguration:
        print(f"No static website configuration found for bucket: {bucket_name}")
        return None
    except Exception as e:
        print(f"Error retrieving website configuration: {e}")
        return None

get_website_configuration('boto3-bucket-02062025')