import boto3

def detach_policy(policy_arn, user_name):
    iam = boto3.client('iam')

    response = iam.detach_user_policy(
        UserName = user_name,
        PolicyArn = policy_arn
    )

    print(response)

detach_policy('arn:aws:iam::577638393014:policy/PyBoto3access', 'boto3_user')