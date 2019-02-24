from boto3.dynamodb.conditions import Key, Attr
import boto3
 

def get_users(config):
    session = boto3.Session(
        aws_access_key_id = config["aws"]["AwsAccessKeyId"],
        aws_secret_access_key=config["aws"]["AwsSecretAccessKey"],
    )

    dynamodb = session.resource('dynamodb')
    WordsTable = 'SurveyUsers'
    table = dynamodb.Table(WordsTable)

    response = table.scan()
    
    # list users:
    #users = [item[] for item in response['Items']]
    return response['Items']