import boto3

def delete_user(user_name):
    iam = boto3.client('iam')
    response = iam.delete_user(UserName=user_name)
    print(response)

delete_user('boto3_user2')