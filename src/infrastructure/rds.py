import boto3

client = boto3.client('rds')


def get_rds_instances():
    response = client.describe_db_instances()
    return response


def stop_rds_instance(identifier):
    response = client.stop_db_instance(
        DBInstanceIdentifier=identifier
    )
    return response
