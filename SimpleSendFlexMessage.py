#linebotapiのインポート
from linebot import LineBotApi
from linebot.models import  FlexSendMessage
import json
import os
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
        "text": "question",
        "wrap": true,
        "align": "center",
        "contents": [
          {
            "type": "span",
            "text": "ELBをパブリックサブネットに配置しその後ろにEC2を配置することで、EC2インスタンス上に構成したWebサービスをインターネット上に公開しています。EC2の配置先として適切なサブネットのタイプはどれでしょうか？  ",
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
            "text": "1.パブリックサブネット",
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
            "text": "2.プライベートサブネット",
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
            "text": "3.VPCエンドポイントが設定されたプライベートサブネット",
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
            "text": "4.オンプレとの専用線接続が設定されたプライベートサブネット",
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

LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
LINE_USER_ID = os.getenv('LINE_USER_ID', None)

# 送信するFlexMessage を作成
line_bot_api.push_message(LINE_USER_ID,flex_message_obj)
