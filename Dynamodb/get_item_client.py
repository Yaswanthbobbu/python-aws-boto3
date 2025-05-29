import boto3


db = boto3.client('dynamodb', region_name='us-east-1')

def get_item(table_name, key):
    try:
        response = db.get_item(TableName=table_name, Key=key)
        print(response.get('Item'))
        return response.get('Item')
    except Exception as e:
        print(f"Error retrieving item: {e}")
        return None

get_item('boto3-table', {'ID': {'S': '3'}})