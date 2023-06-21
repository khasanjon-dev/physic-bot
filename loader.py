import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
