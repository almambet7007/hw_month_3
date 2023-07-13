from config import bot
from aiogram import  types, Dispatcher
from database.sql_commands import  Database

async def filter_messages(message: types.Message):
    '''
    функция которая ловит маты
    '''
    ban_words = ["bitch", "damn", "fuck"]
    if message.chat.type != -1001953753607:
        for i in ban_words :
            if i in message.text.lower().replace(' ', ''):
                await message.reply(text=f' {message.from_user.first_name} отправил '
                                         f'запрещённое слово\n'
                                         f'Админы удалять {message.from_user.first_name}: да/нет')
                break


async def yes_no(message: types.Message):
    if message.chat.type != -1001953753607:
        admin_ans = await check_user_is_admin(message)
        print(admin_ans)
        if admin_ans and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )
check_user_is_admin = bot




# await  bot.ban_chat_member(chat_id=str(message.chat.id), user_id=str(message.reply_to_message.from_user.id)
#
#
#
# async def users_in_ban(message: types.Message):
#     if message.from_user ==
#     username = message.from_user.username
#     first_name = message.from_user.first_name
#     last_name = message.from_user.last_name
#     Database().sql_insert_ban(username=username,
#                                 first_name=first_name,
#                                 last_name=last_name)