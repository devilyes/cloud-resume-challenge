import boto3
import json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-challenge')

def lambda_handler(event, context):
    response = table.update_item(     
        Key={        
            'ID': 'visitors'
        },   
        UpdateExpression='ADD ' + 'visitors' + ' :incr',
        ExpressionAttributeValues={        
            ':incr': 1    
        },    
        ReturnValues="UPDATED_NEW"
    )
    return {
         "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*"
            },
        "statusCode": 200,
    }
