from src.infrastructure import ec2, slack
from src.common import env


def absolutely_stop(event, context):
    changed = []
    unchanged = []
    response = ec2.get_ec2_instances()
    if 'Reservations' in response:
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                if instance['State']['Code'] != 80:
                    ec2.stop_ec2_instance(instance['InstanceId'])
                    changed.append(instance['InstanceId'])
                else:
                    unchanged.append(instance['InstanceId'])
    send_to_slack(changed, unchanged)


def send_to_slack(changed, unchanged):
    fields = [
        {
            'title': 'AWSアカウント名',
            'value': env.get_aws_account_name(),
            'short': True
        },
        {
            'title': 'EC2インスタンスの数',
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

    text = "EC2絶対停止させるマンが起動しました。"
    slack_message = {
        'username': 'Absolutely Stop AWS EC2 Instances',
        'channel': env.get_slack_channel_id(),
        'icon_emoji': ':aws_ec2:',
        'attachments': [
            {
                'color': 'good',
                'text': text,
                'fields': fields
            }
        ]
    }
    slack.send(slack_message)
