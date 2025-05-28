import boto3

def remove_user(user_name, group_name):
    iam = boto3.resource('iam')

    group = iam.Group(group_name)

    response = group.remove_user(
        UserName=user_name
    )

    # iam = boto3.client('iam')
    # response = iam.remove_user_from_group(
    #     GroupName = group_name,
    #     UserName = user_name
    # )

    print(response)

remove_user('boto3_user', 'boto3_group')