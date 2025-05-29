import boto3
from pprint import pprint
from botocore.exceptions import ClientError

def delete_item(title, year, dynamodb=None):
    if dynamodb is None:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('boto3-table2')

    try:
        response = table.delete_item(
            Key={
                'year': year,
                'title': title
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        pprint("DeleteItem succeeded:")
        pprint(response)

delete_item('Now You See Me', 2013)