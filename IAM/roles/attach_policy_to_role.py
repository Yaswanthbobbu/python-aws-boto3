import boto3


def attach_policy_to_role(role_name, policy_arn):
    iam = boto3.client('iam')

    response = iam.attach_role_policy(
        RoleName=role_name,
        PolicyArn=policy_arn
    )

    print(response)

attach_policy_to_role('MyNewRole', 'arn:aws:iam::577638393014:policy/PyBoto3access')