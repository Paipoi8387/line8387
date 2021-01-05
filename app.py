from flask import Flask, request, abort
from linebot import (
        　LineBotApi, WebhookHandler
        )
from linebot.exceptions import (
        　InvalidSignatureError
        )
from linebot.models import (
        　MessageEvent, TextMessage, TextSendMessage
        )

app = Flask(__name__)

ACCESS_TOKEN = Hn2OOEvFVTl3aMSYhHJXfucVLVJLgodZBkc7CMKEx8YgGlSpOeekx+qV/NxjQLXFUx+LhgpeuxctLzbrbo9kwqsDhwg9uJM75wcITCKygM3PKdxOfSeuze2rcbWI+qIezHVI2XJ8Rd6PA7ptnyThKQdB04t89/1O/w1cDnyilFU= 
SECRET = 9be3d4a4164ffe583664b29dcb6aa2c0

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route(“/callback”, methods=[‘POST’])
def callback():
    　signature = request.headers[‘X-Line-Signature’] 　body = request.get_data(as_text=True)
    　app.logger.info(“Request body: ” + body)

    　try:
        　　handler.handle(body, signature)
        　except InvalidSignatureError:
            　　abort(400)

            　return ‘OK’

            @handler.add(MessageEvent, message=TextMessage)
            def handle_message(event):
                　line_bot_api.reply_message(
                        　　event.reply_token,
                        　　TextSendMessage(text=event.message.text))

                if __name__ == “__main__”:
                    　app.run()
