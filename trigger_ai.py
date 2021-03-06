import boto3
import os
import json
# STATEMACHINEARN	arn: aws: states: us-east-1: 477880722056: stateMachine: Polyglot-Pipeline
stepfunctions = boto3.client('stepfunctions')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    input = {
        "Bucket" : bucket,
        "Key": key
    }

    response = stepfunctions.start_execution(
        stateMachineArn=os.environ['STATEMACHINEARN'],
        input=json.dumps(input)
    )

    return json.dumps(response, default=str)
