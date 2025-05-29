import boto3
from decimal import Decimal
from pprint import pprint

def update_table_data(title, year, rating, plot, dynamodb=None):
    if dynamodb is None:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('boto3-table2')

    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p",
        ExpressionAttributeValues={
            ':r': Decimal(rating),
            ':p': plot
        },
        ReturnValues="UPDATED_NEW"
    )

    print("UpdateItem succeeded:")
    pprint(response)

update_table_data('Rush', 2013, 10, 'Great movie thriller')