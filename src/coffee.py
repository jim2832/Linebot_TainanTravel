from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import requests
import random
import json
import math
import time
import datetime

#---------------- self define module ----------------
import text_push as text_push
import text_reply as text_reply

#---------------- self define variables ----------------
from mykey import *

#---------------- line settings ----------------
# Channel Access Token
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(LINE_CHANNEL_SECRET)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
cafe1 = "秘氏咖啡"
cafe2 = "Error22 鼴鼠"
cafe3 = "kokoni café"
cafe4 = "a Room 房間咖啡"
cafe5 = "離島咖啡"
cafe6 = "ALFEE Coffee"
cafe7 = "果核抵家"
cafe8 = "任事咖啡"
cafe9 = "二子咖啡"
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#多頁圖片
def cafe_image_carousel():
    output_message = TemplateSendMessage(
        alt_text = "此裝置不支援樣板。", #無法支援格式所顯示的文字
        template = ImageCarouselTemplate(
            columns = [
                #1
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/IKXqxeb.jpg",
                    action = MessageTemplateAction(
                        label = f"{cafe1}",
                        text = f"{cafe1}資訊"
                    )
                ),
                #2
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/ISEjZL2.jpg",
                    action = MessageTemplateAction(
                        label = f"{cafe2}",
                        text = f"{cafe2}資訊"
                    )
                ),
                #3
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/Fa0dLhW.jpg",
                    action = MessageTemplateAction(
                        label = f"{cafe3}",
                        text = f"{cafe3}資訊"
                    )
                ),
                #4
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/ZlyFoay.jpg",
                    action = MessageTemplateAction(
                        label = f"{cafe4}",
                        text = f"{cafe4}資訊"
                    )
                ),
                #5
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/RLSJcX7.jpg",
                    action = MessageTemplateAction(
                        label = f"{cafe5}",
                        text = f"{cafe5}資訊"
                    )
                ),
                #6
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/TWhOlTg.jpg",
                    action = MessageTemplateAction(
                        label = f"{cafe6}",
                        text = f"{cafe6}資訊"
                    )
                ),
                #7
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/ObCZYq1.jpg",
                    action = MessageTemplateAction(
                        label = f"{cafe7}",
                        text = f"{cafe7}資訊"
                    )
                ),
                #8
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/O1TRrmP.jpg",
                    action = MessageTemplateAction(
                        label = f"{cafe8}",
                        text = f"{cafe8}資訊"
                    )
                ),
                #9
                ImageCarouselColumn(
                    image_url = "https://i.imgur.com/mhuLP4k.jpg",
                    action = MessageTemplateAction(
                        label = f"{cafe9}",
                        text = f"{cafe9}資訊"
                    )
                )
            ]
        )
    )
    return output_message

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------