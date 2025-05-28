import boto3

def attach_policy(policy_arn, user_name):
    iam = boto3.client('iam')

    response = iam.attach_user_policy(
        UserName = user_name,
        PolicyArn = policy_arn
    )

    print(response)

attach_policy('arn:aws:iam::577638393014:policy/PyBoto3access', 'boto3_user')