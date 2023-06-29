import os

from aiogram.types import Message, ContentType
from dotenv import load_dotenv

from loader import bot, dp

load_dotenv()
ADMIN_IDS = os.getenv('ADMIN_ID').split(',')
ADMIN_IDS = [int(_id) for _id in ADMIN_IDS if _id]


@dp.message_handler(content_types=ContentType.PHOTO, chat_id=ADMIN_IDS)
async def admin_send_photo(msg: Message):
    photo_file_id = msg.photo[-1].file_id
    text = msg.caption
    try:
        await bot.send_photo(msg.reply_to_message.forward_from.id, photo=photo_file_id, caption=text)
    except:
        pass


@dp.message_handler(chat_id=ADMIN_IDS)
async def admin_message(msg: Message):
    try:
        await bot.send_message(msg.reply_to_message.forward_from.id, msg.text)
    except Exception as e:
        print(e)
