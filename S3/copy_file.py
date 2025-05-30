import boto3


def copy_file(file_name, bucket_name):
    s3_resource = boto3.resource('s3', 'us-east-1')
    copy_source = {
        'Bucket': bucket_name,
        'Key': file_name
    }
    s3_resource.meta.client.copy(copy_source, 'sample-boto3-bucket-python', 'copied.txt')

copy_file('sample-boto3-bucket-python', 'test-sample.docx')

##

