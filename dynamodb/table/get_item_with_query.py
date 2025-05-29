import boto3
from boto3.dynamodb.conditions import Key

def query_movie(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('boto3-table2')

    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )

    return response['Items']

movies = query_movie(1997)

for movie in movies:
    print(movie['year'], " : ", movie['title'])
