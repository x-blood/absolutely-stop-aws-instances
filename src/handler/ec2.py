from src.services import ec2


def lambda_handler(event, context):
    ec2.absolutely_stop(event, context)
