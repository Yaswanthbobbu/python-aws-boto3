import json
import boto3


def create_policy(policy_name):
    iam = boto3.client('iam')

    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "S3:GetObject",
                "Resource": "arn:aws:s3:::sample-boto3-bucket-python/*"
            }
        ]
    }

    response = iam.create_policy(
        PolicyName=policy_name,
        PolicyDocument=json.dumps(policy))

    print(response)

create_policy('PyBoto3access')