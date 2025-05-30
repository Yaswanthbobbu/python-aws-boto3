import boto3

s3_resource = boto3.resource('s3', 'us-east-1')

def get_summary(bucket_name, file_name):
    response = s3_resource.ObjectSummary(bucket_name, file_name)
    print(response)

get_summary('sample-boto3-bucket-python', 'file.txt')
