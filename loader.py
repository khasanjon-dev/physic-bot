import logging

from aiogram import Bot, Dispatcher

API_TOKEN = '5927474751:AAF53TaZ4VtxIB5wlIfHD5l-YZpbziw2DJ4'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
