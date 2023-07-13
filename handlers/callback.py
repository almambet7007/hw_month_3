from config import bot
from aiogram import types, Dispatcher
from database.sql_commands import Database
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup


async def list_of_users(call: types.CallbackQuery):
    users = Database().sql_select_user()
    print(users)
    print(str(users))
    data = []
    for i in users:
        data.append(str(i))
    data = '\n'.join(data)
    await call.message.reply(f"{data}")


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(list_of_users, lambda call: call.data == "list_of_users")
