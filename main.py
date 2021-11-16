#linebotapiのインポート
from linebot import LineBotApi
from linebot.models import  FlexSendMessage
import json
import os

# FlexMessageを送信するスクリプト

LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

LINE_USER_ID = os.getenv('LINE_USER_ID', None)

print('Send Flex Message')

flex_message = """
{
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "問題",
        "size": "lg",
        "align": "center"
      }
    ],
    "position": "relative",
    "margin": "md"
  },
  "hero": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "問題",
        "wrap": true,
        "align": "center",
        "contents": [
          {
            "type": "span",
            "text": "おかえりなさい",
            "size": "md"
          }
        ],
        "weight": "regular"
      },
      {
        "type": "text",
        "text": "answer1",
        "contents": [
          {
            "type": "span",
            "text": "1.ごはんにする？",
            "size": "md"
          }
        ],
        "align": "center",
        "margin": "xxl"
      },
      {
        "type": "text",
        "text": "answer2",
        "contents": [
          {
            "type": "span",
            "text": "2.お風呂にする",
            "size": "md"
          }
        ],
        "align": "center",
        "margin": "xxl"
      },
      {
        "type": "text",
        "text": "answer3",
        "contents": [
          {
            "type": "span",
            "text": "3.それともアタタタタタタタ！！！！",
            "size": "md"
          }
        ],
        "margin": "xxl",
        "align": "center",
        "wrap": true
      },
      {
        "type": "text",
        "text": "answer4",
        "contents": [
          {
            "type": "span",
            "text": " 4.北斗百裂拳",
            "size": "md"
          }
        ],
        "align": "center",
        "wrap": true,
        "margin": "xxl"
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "<1>",
          "uri": "http://linecorp.com/"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "<2>",
          "uri": "http://linecorp.com/"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "<3>",
          "uri": "http://linecorp.com/"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "<4>",
          "uri": "http://linecorp.com/"
        }
      }
    ],
    "background": {
      "type": "linearGradient",
      "angle": "200deg",
      "startColor": "#ffa500",
      "endColor": "#ffa500"
    }
  }
}
"""
flex_message_json_dict = json.loads(flex_message)

# 送信するFlexMessage を作成
line_bot_api.push_message(
  LINE_USER_ID,
  FlexSendMessage(
      alt_text='alt_text',
      # contentsパラメタに, dict型の値を渡す
      contents=flex_message_json_dict
  )
)