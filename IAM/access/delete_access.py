import boto3

def delete_access(user_name):
    iam = boto3.client('iam')
    response = iam.delete_access_key(
        UserName=user_name,
        AccessKeyId='AKIAYM7POMS3HTGMLANY'
    )
    print(response)

delete_access('boto3_user')

