import boto3


def add_tags_to_user():
    iam = boto3.client('iam')
    user_name = 'cli-user'
    tags = [{'Key': 'Department', 'Value': 'Engineering'},{'Key': 'Project', 'Value': 'AI Research'}]
    response = iam.tag_user(
        UserName=user_name,
        Tags=tags,
    )
    print(f"Tags added to user {user_name}: {response}")


add_tags_to_user()