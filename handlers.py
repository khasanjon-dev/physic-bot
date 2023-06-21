import os

from aiogram import types
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from aiogram.types import Message

from loader import dp, bot

ADMIN_IDS = os.getenv('ADMIN_ID').split(',')


@dp.message_handler(CommandStart())
async def send_welcome(message: Message):
    text = f"Assalomu alaykum {message.from_user.first_name} !"
    await message.answer(text)
    text = "Savolingizni yozing va biz sizga imkon qadar tez orada javob beramiz."
    await message.answer(text)


@dp.message_handler(CommandHelp())
async def help_message(msg: Message):
    text = "Savolingizni yozing va biz sizga imkon qadar tez orada javob beramiz."
    await msg.answer(text)


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def send_photo(msg: Message):
    photo_file_id = msg.photo[-1].file_id
    text = f"Xabar {msg.from_user.first_name} dan yuborildi !\n" \
           f"@{msg.from_user.username}"
    text += f"\n\n{msg.caption}"
    for admin_id in ADMIN_IDS:
        await bot.send_photo(admin_id, photo=photo_file_id, caption=text)
    await msg.answer('rasm adminga yuborildi 🙂')


@dp.message_handler()
async def response(msg: Message):
    text = f"{msg.from_user.first_name} dan\n\n" \
           f"{msg.text}"
    for admin_id in ADMIN_IDS:
        await bot.send_message(admin_id, text)
    await msg.answer('xabar adminga yuborildi 😊')
