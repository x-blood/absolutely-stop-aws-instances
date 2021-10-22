import boto3

client = boto3.client('ec2')


def get_ec2_instances():
    response = client.describe_instances()
    return response


def stop_ec2_instance(instance_id):
    response = client.stop_instances(
        InstanceIds=[
            instance_id
        ]
    )
    return response
