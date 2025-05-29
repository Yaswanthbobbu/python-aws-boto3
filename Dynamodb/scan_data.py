from pprint import pprint
import boto3

db = boto3.resource('dynamodb', region_name='us-east-1')

def scan_table(table_name):
    table = db.Table(table_name)
    response = table.scan()
    data = response.get('Items', [])

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response.get('Items', []))

    pprint(data)

scan_table(table_name='boto3-table')