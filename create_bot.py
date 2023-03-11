from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


API_TOKEN = ''
storage = MemoryStorage()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

