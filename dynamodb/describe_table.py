import boto3
from pprint import pprint

db = boto3.client('dynamodb', region_name='us-east-1')

def describe_table():
    response = db.describe_table(TableName='boto3-table')
    pprint(response)

describe_table()
