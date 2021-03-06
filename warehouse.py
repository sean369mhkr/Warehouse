from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import configparser
import Postgres
config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token')) #Channel access token
handler = WebhookHandler(config.get('line-bot', 'channel_secret')) #Channel secret

@app.route("/")
def home():
    return "<h1>Welcome to CodingX</h1>"
    # return render_template("home.html")
# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# 學你說話
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text[0]=="#":
        sql=Postgres.main(event.message.text)
        if event.message.text[1]=="+":
            get_V=sql.add()
        elif event.message.text[1]=="-":
            get_V=sql.reduce()
        elif event.message.text[1].upper()=="R":
            get_V=sql.read()
        else:
            get_V=sql.ntype()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=get_V))
    elif event.message.text=="My info":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(event)))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()

