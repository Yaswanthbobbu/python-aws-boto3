import boto3

def create_access(user_name):
    iam = boto3.client('iam')
    response = iam.create_access_key(UserName=user_name)
    print(response)

create_access('boto3_user')


# def update_access(user_name):
#     iam = boto3.client('iam')
#     response = iam.update_access_key(
#         AccessKeyId='AKIAYM7POMS3FXOXQKXL',
#         Status='Inactive',
#         UserName=user_name,
#     )
#
#     print(response)
#
# update_access('boto3_user')