# line_flex_message_local

LINE Bot に対して FlexMessage を送る(ローカル版)

## 動作環境

- Python 3.9.6
- Windows10 Pro
  - Windows Update 20H2

## 使い方

```bash
git clone https://github.com/ymd65536/line_flex_message_local.git
cd line_flex_message_local
pip install line-bot-sdk -t .
python main.py
```

環境変数を設定する。

```.env
LINE_USER_ID=YOUR_LINE_USER_ID
LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN
```

`YOUR_LINE_USER_ID` には LINE MessagingAPI から取得できる「あなたのユーザ ID」  
`YOUR_LINE_CHANNEL_ACCESS_TOKEN` には LINE MessagingAPI から取得できる「チャネルアクセストークン」
