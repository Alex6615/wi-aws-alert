from telegram import Update
from telegram.ext import Application
# ENV
import os
TELEGRAM_TOKEN = os.getenv(key="TELEGRAM_TOKEN")
TGCHATID = os.getenv(key='TGCHATID')
CF_TOPIC = os.getenv(key='CF_TOPIC')



class telegramBotTools :
    def __init__(self):
        self.application = Application.builder().token(TELEGRAM_TOKEN).build()

    @classmethod
    async def sendCFMessage(cls, msg):
        self = telegramBotTools()
        msg = msg.replace('-','\-').replace('.','\.')
        print(msg)
        await self.application.bot.send_message(
           chat_id=TGCHATID,
           message_thread_id=CF_TOPIC,
           text = msg,
           parse_mode='MARKDOWNV2',
        )

if __name__ == "__main__" :
    pass