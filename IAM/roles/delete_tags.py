import boto3


def remove_tags(user_name, tags):
    iam = boto3.client('iam')

    response = iam.untag_user(
        UserName=user_name,
        TagKeys=tags
    )

    print(f"Tags removed from user {user_name}: {response}")

remove_tags('cli-user', ['Department', 'Project'])