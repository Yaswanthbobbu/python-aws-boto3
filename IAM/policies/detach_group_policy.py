import boto3

def detach_group_policy(policy_arn, group_name):
    iam = boto3.client('iam')

    response = iam.detach_group_policy(
        GroupName = group_name,
        PolicyArn = policy_arn
    )

    print(response)

detach_group_policy('arn:aws:iam::577638393014:policy/PyBoto3access', 'boto3_group')