#linebotapiのインポート
from linebot import LineBotApi
from linebot.models import  FlexSendMessage
import json
import os

# FlexMessageを送信するスクリプト

LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

LINE_USER_ID = os.getenv('LINE_USER_ID', None)

print('Send Flex Message DynamoDB')

flex_message = ""

flex_message_json_dict = json.loads(flex_message)

flex_message_obj = FlexSendMessage(
    alt_text='alt_text',
    # contentsパラメタに, dict型の値を渡す
    contents=flex_message_json_dict
)

# 送信するFlexMessage を作成
line_bot_api.push_message(LINE_USER_ID,flex_message_obj)
