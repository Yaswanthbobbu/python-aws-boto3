import boto3
from botocore.exceptions import ClientError

def delete_table(table_name):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    try:
        table = dynamodb.Table(table_name)
        response = table.delete()
        print(f"Delete table response: {response}")
    except ClientError as e:
        print(f"Error deleting table {table_name}: {e.response['Error']['Message']}")
    else:
        print(f"Table {table_name} deleted successfully.")

delete_table('boto3-table')  # Replace with your table name