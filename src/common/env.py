import os


def get_slack_channel_id():
    return os.environ['SLACK_CHANNEL_ID']


def get_slack_web_hook_url():
    return os.environ['SLACK_WEB_HOOK_URL']


def get_aws_account_name():
    return os.environ['AWS_ACCOUNT_NAME']
