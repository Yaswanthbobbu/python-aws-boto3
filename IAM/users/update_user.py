import boto3

def update_user(old_name, new_name):
    iam = boto3.client('iam')
    response = iam.update_user(UserName=old_name, NewUserName=new_name)
    print(response)

update_user('boto3_user2', 'boto3_user_update')