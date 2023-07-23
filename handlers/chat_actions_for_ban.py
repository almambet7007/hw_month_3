# from aiogram import types, Dispatcher
# from database.sql_commands import Database
# from config import bot

# ban_amount_limited = 0


# async def real_ban(message: types.Message):
#     ban_words = [
#         "mature",
#         "afraid",
#         "global",
#         "mountains"
#     ]
#     if message.chat.id == -935883341:
#         # global ban_amount_limited
#         for i in ban_words:
#             if i in message.text.lower().replace(" ", ""):
#                 await message.reply(f"{message.from_user.username} send bad message\n"
#                                     f"admin please delete {message.from_user.username}:yes/no")
#                 # await ban_amount_limited += 1
#                 # await Database().sql_insert_ban_table(id=message.from_user.id,
#                 #                                       username=message.from_user.username,
#                 #                                       ban_amount=ban_amount_limited,)
#
#
#
# async def checking_for_yes_no(message: types.Message):
#     if message.chat.id == -935883341:
#         admin_ans = await check_user_is_admin(message)
#         print(admin_ans)
#         if admin_ans and message.reply_to_message:
#             await message.bot.ban_chat_member(
#                 chat_id=message.chat.id,
#                 user_id=message.reply_to_message.from_user.id
#             )
#
# check_user_is_admin = bot
#
# # async def send_users_in_ban_list(message: types.Message):
# #     id = message.from_user.id
# #     username = message.from_user.username
# #     ban_amount = ban_amount_limited
# #     Database().sql_insert_ban_table(id=id,
# #                                     username=username,
# #                                     ban_amount=ban_amount)
#
#
# def register_handlers_chat_actions_for_ban(dp: Dispatcher):
#     dp.register_message_handler(real_ban)
#     dp.register_message_handler(checking_for_yes_no)
