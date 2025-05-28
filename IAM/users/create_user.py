import boto3

def create_user(user_name):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=user_name)
    print(response)

create_user('boto3_user2')