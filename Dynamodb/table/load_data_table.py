import boto3
import json
from decimal import Decimal

def load_table(table_name, data_file):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table(table_name)

    with table.batch_writer() as batch:
        for item in data_file:
            batch.put_item(Item=item)

    print(f"Data loaded into {table_name} successfully.")

load_table('boto3-table2', data_file=json.load(open('movie_data.json'), parse_float=Decimal))

