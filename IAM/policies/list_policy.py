import boto3

def list_policy():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_policies')

    for resp in paginator.paginate(Scope='Local'):
        for policy in resp['Policies']:
            name = policy['PolicyName']
            arn = policy['Arn']
            print(f'Name: {name}, Arn: {arn}')

list_policy()