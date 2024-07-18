import asyncio
from telegram import Bot
import time

# Replace 'YOUR_TOKEN' with your bot's token
bot = Bot(token='<BOT-TOKEN>')


# Replace 'CHAT_ID' with the actual chat ID
# To get the chat ID, add @RawDataBot(to find remote group's ChatID) or Telegram Bot Raw(to find own chat-id) and get the chat ID

chat_id = 'XXXXXXXXXX' 


# The message you want to send
message_text = 'Hey!'

async def send_async_message():
    # Sending the message
    await bot.send_message(chat_id=chat_id, text=message_text)

# Running the asynchronous function
if __name__ == "__main__":
    asyncio.run(send_async_message())
