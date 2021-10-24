from src.services import rds


def lambda_handler(event, context):
    rds.absolutely_stop(event, context)
