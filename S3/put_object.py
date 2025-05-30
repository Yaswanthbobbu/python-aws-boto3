import boto3

bucket = boto3.client('s3', region_name='us-east-1')

def put_data(bucket_name, data_item):
    response = bucket.put_object(
        ACL="private",
        Bucket=bucket_name,
        Body=data_item,
        Key='aws.jpg'
    )

    print(response)

with open('aws.jpg', 'rb') as f:
    data = f.read()

put_data('file.txt', 'sample-boto3-bucket-python')