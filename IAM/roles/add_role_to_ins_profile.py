import boto3

def add_role_to_instance_profile(profile_name, role_name):
    iam = boto3.client('iam')

    try:
        response = iam.add_role_to_instance_profile(
            InstanceProfileName=profile_name,
            RoleName=role_name
        )
        print(f"Role '{role_name}' added to instance profile '{profile_name}' successfully.")
        return response
    except Exception as e:
        print(f"Error adding role to instance profile: {e}")
        return None

add_role_to_instance_profile("boto3_instance_profile", "MyNewRole")