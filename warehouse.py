from __future__ import unicode_literals
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('QWkFT44dkUM3TsCvNQUG8XHkAWAc1cVD2SISNjMeYttWbUGA476WTF4vSpEglds1FLIFOo18qXD4l8OriJiVDtegPxtzfHkTKZqA9ADp6fG8suDLISzZLTKc4x7K2JWmvdpYCYYMAToRZQPo7IMNUgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('58c2f6775b9492c2da817c73d37e6f9b')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    # if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )

if __name__ == "__main__":
    app.run()

