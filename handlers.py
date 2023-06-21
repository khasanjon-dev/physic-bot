import os

from aiogram.dispatcher.filters import CommandStart, CommandHelp
from aiogram.types import Message

from loader import dp, bot

ADMIN_ID = os.getenv('admin_id')


@dp.message_handler(CommandStart())
async def send_welcome(message: Message):
    text = f"Assalomu alaykum {message.from_user.first_name} !"
    await message.answer(text)
    text = "Savolingizni yozing va biz sizga imkon qadar tez orada javob beramiz."
    await message.answer(text)


@dp.message_handler(CommandHelp())
async def help_message(message: Message):
    text = "Savolingizni yozing va biz sizga imkon qadar tez orada javob beramiz."
    await message.answer(text)



@dp.message_handler(content_types=)


@dp.message_handler()
async def response(msg: Message):
    text = "Savol adminga yuborildi 😊"
    bot.send_message(ADMIN_ID, msg.text)
    await msg.reply(text)
