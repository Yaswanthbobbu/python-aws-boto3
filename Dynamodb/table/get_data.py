import boto3
from pprint import pprint
from botocore.exceptions import ClientError

def get_table_data(title, year, dyanmodb=None):
    if dyanmodb is None:
        dyanmodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dyanmodb.Table('boto3-table2')
    try:
        response = table.get_item(
            Key={
                'year': year,
                'title': title
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response.get('Item')
        if item:
            pprint(item)
        else:
            pprint("No item found with the specified key.")

get_table_data('Rush', 2013)