import boto3


def list_tags():
    iam = boto3.client('iam')
    response = iam.list_users()

    for user in response['Users']:
        user_name = user['UserName']
        tags = iam.list_user_tags(UserName=user_name)
        print(f"User: {user_name}, Tags: {tags['Tags']}")

list_tags()
