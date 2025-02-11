from telegram import Update
from telegram.ext import Application
# ENV
import os
TELEGRAM_TOKEN = os.getenv(key="TELEGRAM_TOKEN")
TGCHATID = os.getenv(key='TGCHATID')
TOPIC = os.getenv(key='TOPIC')



class telegramBotTools :
    def __init__(self):
        self.application = Application.builder().token(TELEGRAM_TOKEN).build()

    @classmethod
    async def sendMessage(cls, msg):
        self = telegramBotTools()
        msg = msg.replace('-','\-').replace('.','\.')
        print(msg)
        await self.application.bot.send_message(
           chat_id=TGCHATID,
           message_thread_id=TOPIC,
           text = msg,
           parse_mode='MARKDOWNV2',
        )

if __name__ == "__main__" :
    import asyncio
    text = f"➖ *Daily Traffic* Now is Over 2.1278 Terabyte\n \
            ➖ *CPU* Loading Now [11.41]%\n \
            ➖ *MEM* Loading Now [11.36]%"
    asyncio.run(test(text))