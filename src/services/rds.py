from src.infrastructure import rds, slack
from src.common import env


def absolutely_stop(event, context):
    changed = []
    unchanged = []
    response = rds.get_rds_instances()
    if 'DBInstances' in response:
        for instance in response['DBInstances']:
            if instance['DBInstanceStatus'] != "stopped":
                rds.stop_rds_instance(instance['DBInstanceIdentifier'])
                changed.append(instance['DBInstanceIdentifier'])
            else:
                unchanged.append(instance['DBInstanceIdentifier'])
    send_to_slack(changed, unchanged)


def send_to_slack(changed, unchanged):
    fields = [
        {
            'title': 'AWSアカウント名',
            'value': env.get_aws_account_name(),
            'short': True
        },
        {
            'title': 'RDSインスタンスの数',
            'value': len(changed) + len(unchanged),
            'short': True
        }
    ]
    if len(changed) != 0:
        fields.append({
            'title': '停止したインスタンスIDs',
            'value': "\n".join(changed),
            'short': False
        })
    if len(unchanged) != 0:
        fields.append({
            'title': '停止済みのインスタンスIDs',
            'value': "\n".join(unchanged)
        })

    text = "RDS絶対停止させるマンが起動しました。"
    slack_message = {
        'username': 'Absolutely Stop RDS Instances',
        'channel': env.get_slack_channel_id(),
        'icon_emoji': ':aws_rds',
        'attachments': [
            {
                'color': 'good',
                'text': text,
                'fields': fields
            }
        ]
    }
    slack.send(slack_message)
