from aiogram import types,Dispatcher
from database.sql_commands import  Database
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

async def list_of_users(call: types.CallbackQuery):
   users = Database().sql_select_user()
   print(users)
   print(str(users))
   data = []
   for user in users:
       if not user["username"]:
          data.append("None Username")
       else:
           data.append(user["username"])

   data = '\n'.join(data)
   await call.message.reply(data)

async def list_of_poll_user(call: types.CallbackQuery):
   users = Database().sql_select_user_form()
   print(users)
   print(str(users))
   data = []
   for user in users:
       if not user["username"]:
           data.append("None Username")
       else:
           data.append(user["username"])

   data = '\n'.join(data)
   await call.message.reply(data)






def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(list_of_users, lambda call: call.data == "list_of_users")
    dp.register_message_handler(list_of_poll_user, lambda call: call.data == "list_of_poll_user")

