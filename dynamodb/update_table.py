import boto3

db = boto3.client('dynamodb', region_name='us-east-1')

def update_table(table_name, new_read_capacity, new_write_capacity):
    try:
        response = db.update_table(
            TableName=table_name,
            BillingMode='PROVISIONED',
            ProvisionedThroughput={
                'ReadCapacityUnits': new_read_capacity,
                'WriteCapacityUnits': new_write_capacity
            }
        )
        print(f"Table {table_name} updated successfully.")
        return response
    except Exception as e:
        print(f"Error updating table {table_name}: {e}")
        return None

update_table('boto3-table', 1, 1)