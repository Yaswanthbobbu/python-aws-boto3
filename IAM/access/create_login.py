import boto3

def create_login(user_name):
    iam = boto3.client('iam')

    response = iam.create_login_profile(
        Password ='Password@1',
        PasswordResetRequired=False,
        UserName=user_name
    )

    print(response)

create_login('boto3_user')