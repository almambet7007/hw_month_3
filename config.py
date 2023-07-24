from decouple import  config
from  aiogram import  Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import  MemoryStorage

admin = (1036061654,
         2110846780)

storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

