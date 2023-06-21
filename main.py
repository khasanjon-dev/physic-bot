from aiogram.utils import executor

import handlers  # noqa
from commands import set_default_commands
from loader import dp


async def on_startup(dp):
    await set_default_commands(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
