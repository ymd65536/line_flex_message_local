from boto3.session import Session
import json
import os

AWS_ACCESS_KEY_ID=os.getenv('AWS_ACCESS_KEY_ID',None)
AWS_SECRET_ACCESS_KEY=os.getenv('AWS_SECRET_ACCESS_KEY',None)
table_name = 'AwsQuiz'

def get_dynamo_table(key_id, access_key, table_name):
    session = Session(
            aws_access_key_id=key_id,
            aws_secret_access_key=access_key,
            region_name='ap-northeast-1'
    )
 
    dynamodb = session.resource('dynamodb')
    dynamo_table = dynamodb.Table(table_name)
    return dynamo_table
 
def insert_data_from_json(table, input_file_name):
    with open(input_file_name, "r",encoding="utf-8") as f:
        json_data = json.load(f)
        with table.batch_writer() as batch:
            for record in json_data:
                batch.put_item(Item=record)
    print('Successfully inserted data.')
 
if __name__ == '__main__':

    dynamo_table = get_dynamo_table(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, table_name)

    # 問題文データをインポート
    input_file_name = './json/question_1.json' 
    insert_data_from_json(dynamo_table, input_file_name)