import boto3


# db = boto3.resource('dynamodb', region_name='us-east-1')
# table = db.Table('boto3-table')

# def put_data():
#     response = table.put_item(
#         Item={
#             'ID': '1',
#             'name': 'John Doe',
#             'age': 30,
#             'city': 'New York'
#         }
#     )
#     print(response)

db = boto3.client('dynamodb', region_name='us-east-1')
def put_data():
    response = db.put_item(
        TableName='boto3-table',
        Item={
            'ID': {'S': '2'},
            'name': {'S': 'Yash Doe'},
            'age': {'N': '35'},
            'city': {'S': 'India'}

        }
    )
    print(response)

put_data()
