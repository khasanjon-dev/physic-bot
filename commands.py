from aiogram.types import BotCommand


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            BotCommand("start", "Botni ishga tushurish"),
            BotCommand("help", "Yordam"),
        ]
    )
