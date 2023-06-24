import os

from aiogram import types
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from aiogram.types import Message

from loader import dp, bot

ADMIN_IDS = os.getenv('ADMIN_ID').split(',')
ADMIN_IDS = [int(_id) for _id in ADMIN_IDS if _id]


@dp.message_handler(CommandStart())
async def send_welcome(msg: Message):
    hello = f"Assalomu alaykum va rohmatullohi va barokatuh!"
    question = "Sizga qanday yordam bera olishimiz mumkin? \n" \
               "Savolingiz bo‘lsa, marhamat yozing, sizga tez orada javob beramiz."
    await msg.answer(hello)
    await msg.answer(question)


@dp.message_handler(CommandHelp())
async def help_message(msg: Message):
    text = "Savolingizni yozing va biz sizga imkon qadar tez orada javob beramiz."
    await msg.answer(text)


# admin photo
@dp.message_handler(lambda msg: msg.from_user.id in ADMIN_IDS)
@dp.message_handler(content_types=['photo'])
async def send_photo(msg: Message):
    photo_file_id = msg.photo[-1].file_id
    text = msg.caption
    for admin_id in ADMIN_IDS:
        await bot.send_photo(admin_id, photo=photo_file_id, caption=text)
    await msg.answer('rasm adminga yuborildi 🙂')


# admin send message
@dp.message_handler(lambda msg: msg.from_user.id in ADMIN_IDS)
async def admin_message(msg: Message):
    await bot.send_message(msg.reply_to_message.forward_from.id, msg.text)


# user photo
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def send_photo(msg: Message):
    photo_file_id = msg.photo[-1].file_id
    text = msg.caption
    for admin_id in ADMIN_IDS:
        await bot.send_photo(admin_id, photo=photo_file_id, caption=text)
    await msg.answer('rasm adminga yuborildi 🙂')


# user message
@dp.message_handler()
async def response(msg: Message):
    for admin_id in ADMIN_IDS:
        await bot.forward_message(admin_id, msg.chat.id, msg.message_id)
    await msg.answer('xabar adminga yuborildi 😊')
