import json
import boto3


def create_policy():
    iam = boto3.client('iam')

    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }

    response = iam.create_policy(
        PolicyName='PyBoto3access',
        PolicyDocument=json.dumps(policy))

    print(response)

create_policy()