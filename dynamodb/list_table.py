import boto3

db = boto3.client('dynamodb', region_name='us-east-1')

def list_tables():
    response = db.list_tables()
    print(response['TableNames'])

list_tables()