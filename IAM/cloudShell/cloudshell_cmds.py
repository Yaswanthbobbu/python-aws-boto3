"""
aws --version

aws iam list-users
aws iam list-groups
aws iam list-policies
aws iam create-user --user-name <name>

aws iam create-login-profile --generate-cli-skeleton > create-login.json
aws iam create-login-profile --cli-input-json file://create-login.json

aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --user-name cli-user
aws iam detach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --user-name cli-user

aws iam create-access-key --user-name cli-user
aws iam delete-access-key --user-name cli-user

aws iam create-group --group-name cli-group
aws iam add-user-to-group --user-name cli-user --group-name cli-group
aws iam remove-user-from-group --user-name cli-user --group-name cli-group
aws iam delete-group --group-name cli-group

"""