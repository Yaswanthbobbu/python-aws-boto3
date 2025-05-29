import boto3

def add_user(user_name, group_name):
    iam = boto3.client('iam')

    response = iam.add_user_to_group(
        GroupName = group_name,
        UserName = user_name
    )

    print(response)

add_user('boto3_user', 'boto3_group')