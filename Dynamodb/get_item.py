import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def get_item(table_name, key):
    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(Key=key)
        print(response['Item'])
        return response.get('Item', None)
    except Exception as e:
        print(f"Error retrieving item: {e}")
        return None

get_item('boto3-table', {'ID': '2'})