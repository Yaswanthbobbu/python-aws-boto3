import boto3

db = boto3.resource('dynamodb', region_name='us-east-1')
table = db.Table('boto3-table')

def batch_writer_example():
    with table.batch_writer() as batch:
        batch.put_item(
            Item={
                'ID': '3',
                'name': 'John Green',
                'age': 30
            }
        )
        batch.put_item(
            Item={
                'ID': '4',
                'name': 'Jane Smith',
                'age': 25
            }
        )
batch_writer_example()
