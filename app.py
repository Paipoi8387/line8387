from flask import Flask, request, abort
import os
import requests
import bs4

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello world!"

def get_website():
        url = 'https://github.com/Paipoi8387/line8387'
        file = 'hoge.txt'

	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text,'html.parser')# Parser
	elems = soup.select('.limited.rfloat') # class要素の取得
	str_elems = str(elems) # stringに変換
	try:
		f = open(file)
		old_elems  = f.read()
	except:
		old_elems = ' '
	if(str_elems == old_elems):
		return False
	else:
		f = open(file, 'w') # 上書きする
		f.writelines(str_elems)
		f.close()
		return True


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
#    app.run()
    if(get_website()):
        port = int(os.getenv("PORT"))
        app.run(host="0.0.0.0", port=port)
