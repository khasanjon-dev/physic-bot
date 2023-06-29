import os

from aiogram.dispatcher.filters import Text
from aiogram.types import ContentType, Message
from dotenv import load_dotenv

from loader import bot, dp

load_dotenv()
ADMIN_IDS = os.getenv('ADMIN_ID').split(',')
ADMIN_IDS = [int(_id) for _id in ADMIN_IDS if _id]


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo(msg: Message):
    photo_file_id = msg.photo[-1].file_id
    text = f"Forwarded from {msg.from_user.first_name}"
    if mes := msg.caption:
        text += f"\n{mes}"
    for admin_id in ADMIN_IDS:
        await bot.send_photo(admin_id, photo=photo_file_id, caption=text)
    await msg.answer('rasm adminga yuborildi 🙂')


@dp.message_handler(Text(contains='Assalom', ignore_case=True))
@dp.message_handler(Text(equals='Assalomu alaykum', ignore_case=True))
async def hello_message(msg: Message):
    await msg.reply("Vaalaykum assalom va Rohmatulloh 🙂")


# user message
@dp.message_handler()
async def response(msg: Message):
    for admin_id in ADMIN_IDS:
        await bot.forward_message(admin_id, msg.chat.id, msg.message_id)
    await msg.answer('xabar adminga yuborildi 😊')
