import boto3
from pprint import pprint

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def batch_get_item(table_name):
    keys = [{'ID': '1'}, {'ID': '2'}, {'ID': '3'}]

    try:
        response = dynamodb.batch_get_item(
            RequestItems={
                table_name: {
                    'Keys': keys
                }
            }
        )
        items = response['Responses'][table_name]
        for item in items:
            pprint(item)
        return items
    except Exception as e:
        pprint(f"Error retrieving batch items: {e}")
        return None

batch_get_item(table_name='boto3-table')