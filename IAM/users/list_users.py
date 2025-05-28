import boto3


def list_users():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_users')
    group_dict = {}
    for resp in paginator.paginate():
        for user in resp['Users']:
            group_dict[user['UserName']]=user['Arn']

    print(group_dict)

list_users()

