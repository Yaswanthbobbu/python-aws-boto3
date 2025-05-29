import boto3

db = boto3.client('dynamodb', region_name='us-east-1')

"""
def create_backup(table_name):
    response = db.create_backup(
        TableName=table_name,
        BackupName=f"{table_name}-backup"
    )
    print(response['BackupDetails']['BackupArn'])

create_backup('boto3-table')
"""

def delete_backup(backup_arn):
    try:
        response = db.delete_backup(
            BackupArn=backup_arn
        )
        print(f"Backup {backup_arn} deleted successfully.")
        return response
    except Exception as e:
        print(f"Error deleting backup {backup_arn}: {e}")
        return None

delete_backup('arn:aws:dynamodb:us-east-1:577638393014:table/boto3-table/backup/01748518263860-4d88935b')