import boto3

def create_instance_profile(profile_name):
    iam = boto3.client('iam')

    try:
        response = iam.create_instance_profile(
            InstanceProfileName=profile_name
        )
        print(f"Instance profile '{profile_name}' created successfully.")
        return response
    except Exception as e:
        print(f"Error creating instance profile: {e}")
        return None


create_instance_profile("boto3_instance_profile")