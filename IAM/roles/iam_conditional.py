import json

import boto3
from datetime import datetime

iam = boto3.client('iam')
current_date = datetime.now().strftime("%Y-%m-%d")

start_time = f"{current_date}T00:00:00Z"
end_time = f"{current_date}T02:59:59Z"

policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::sample-boto3-bucket-python/*",
            "Condition": {
                "DateGreaterThan": {"aws:CurrentTime": start_time},
                "DateLessThan": {"aws:CurrentTime": end_time}
            }
        }
    ]
}

response = iam.create_policy(
    PolicyName="boto3-conditional-policy",
    PolicyDocument=json.dumps(policy_document)
)