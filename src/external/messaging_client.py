import json

import boto3
from botocore.config import Config

my_config = Config(
    region_name='us-east-1'
)

sqs_client = boto3.client('sqs', config=my_config)
sns_client = boto3.client('sns', config=my_config)


class MessagingClient:
    @staticmethod
    def send(topic: str, message: dict):
        sns_client.publish(
            TopicArn=topic,
            Message=json.dumps({'default': json.dumps(message)}),
            MessageStructure='json'
        )
