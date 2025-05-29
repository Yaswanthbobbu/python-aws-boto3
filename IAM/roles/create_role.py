import json

import boto3

def create_role(role_name):
    iam = boto3.client('iam')

    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

    try:
        response = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy)
        )
        print("Role created successfully:", response['Role']['Arn'])
    except Exception as e:
        print("Error creating role:", e)


create_role('MyNewRole')

# arn:aws:iam::577638393014:role/MyNewRole

