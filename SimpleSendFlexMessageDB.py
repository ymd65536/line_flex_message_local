#linebotapiのインポート
from linebot import LineBotApi
from linebot.models import  FlexSendMessage
import json
import os

print('Send Flex Message DynamoDB')

# 送信するFlexMessage を作成
flex_message = flex_message = """
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
        "text": "question",
        "wrap": true,
        "align": "center",
        "contents": [
          {
            "type": "span",
            "text": "サンプル問題",
            "size": "md"
          }
        ],
        "weight": "regular"
      },
      {
        "type": "text",
        "text": "1",
        "contents": [
          {
            "type": "span",
            "text": "1.answer",
            "size": "md"
          }
        ],
        "align": "center",
        "margin": "xxl"
      },
      {
        "type": "text",
        "text": "2",
        "contents": [
          {
            "type": "span",
            "text": "2.answer",
            "size": "md"
          }
        ],
        "align": "center",
        "margin": "xxl"
      },
      {
        "type": "text",
        "text": "3",
        "contents": [
          {
            "type": "span",
            "text": "3.answer",
            "size": "md"
          }
        ],
        "margin": "xxl",
        "align": "center",
        "wrap": true
      },
      {
        "type": "text",
        "text": "4",
        "contents": [
          {
            "type": "span",
            "text": "4.answer",
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
flex_message_obj = FlexSendMessage(
    alt_text='alt_text',
    # contentsパラメタに, dict型の値を渡す
    contents=flex_message_json_dict
)

# ヘッダと問題を作成
header_contents_text = 'タイトル'
hero_contents_text = '問題文'

flex_message_json_dict['header']['contents'][0]['text'] = header_contents_text
flex_message_json_dict['hero']['contents'][0]['contents'][0]['text'] = hero_contents_text

# 回答欄を作成
body_contents_dic ={}
body_contents_dic['action']=[
  {"label":"test","uri":"https://example.com"},
  {"label":"test","uri":"https://example.com"},
  {"label":"test","uri":"https://example.com"},
  {"label":"test","uri":"https://example.com"}
]

# 回答欄のBodyを作成
contents = flex_message_json_dict['body']['contents']
for cnt_i in range(len(contents)):
  contents[cnt_i]['action']['label'] = body_contents_dic['action'][cnt_i]['label']
  contents[cnt_i]['action']['uri'] = body_contents_dic['action'][cnt_i]['uri']


LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
LINE_USER_ID = os.getenv('LINE_USER_ID', None)

# FlexMessage を送信
line_bot_api.push_message(LINE_USER_ID,flex_message_obj)