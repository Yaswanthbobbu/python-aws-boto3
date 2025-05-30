import boto3

from IAM.roles.iam_conditional import response

"""
def delete_file(bucket_name, file_name):
    s3_client = boto3.client('s3', 'us-east-1')
    response = s3_client.delete_object(
        Bucket = bucket_name,
        Key= file_name
    )
    print(response)

delete_file('sample-boto3-bucket-python', 'test_sample.docx')
"""

def delete_multiple_files(bucket_name):
    s3_client = boto3.client('s3', 'us-east-1')
    response = s3_client.delete_objects(
        Bucket=bucket_name,
        Delete = {
            'Objects': [
                 {
                    'Key':'file.txt'
                 }

            ]
    }
    )

    print(response)

delete_multiple_files('sample-boto3-bucket-python')


