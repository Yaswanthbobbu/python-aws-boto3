import json
import boto3


def delete_policy(policy_arn):
    iam = boto3.client('iam')

    response = iam.delete_policy(PolicyArn=policy_arn)

    print(response)

delete_policy('arn:aws:iam::577638393014:policy/PyBoto3access')