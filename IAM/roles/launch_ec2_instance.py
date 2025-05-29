import boto3

def launch_ec2_instance(image_id, instance_type, instance_profile_name, region_name):
    ec2 = boto3.client('ec2', region_name=region_name)

    try:
        response = ec2.run_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            # KeyName=key_name,
            # SecurityGroupIds=[security_group_id],
            IamInstanceProfile={
                'Name': instance_profile_name
            },
            MaxCount=1,
            MinCount=1,
        )
        print("EC2 instance launched successfully:", response['Instances'][0]['InstanceId'])
    except Exception as e:
        print("Error launching EC2 instance:", e)

launch_ec2_instance('ami-0953476d60561c955', 't2.micro', 'boto3_instance_profile', 'us-east-1')