import boto3

def delete_login(user_name):
    iam = boto3.client('iam')

    response = iam.delete_login_profile(
        UserName=user_name
    )

    print(response)

delete_login('boto3_user')