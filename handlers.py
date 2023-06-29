from aiogram.dispatcher.filters import CommandStart, CommandHelp
from aiogram.types import Message

from loader import dp


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


# admin handler
from admin_handler import *  # noqa

# user handler
from user_handler import *  # noqa
