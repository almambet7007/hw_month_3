from aiogram import  types, Dispatcher
from config import  bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.sql_commands import Database
from datetime import datetime, timedelta

async def secret_word(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Список пользователей",
        callback_data="list_of_users"
    )
    markup.add(button_call_1)
    if message.chat.id != -1001953753607:
        await message.reply("ehalo boss, Ehaloooooooo!!!",
                            reply_markup=markup) #является кнопкой (список пользователей) у сообщения






async def echo_ban(message:types.Message):
    ban_words = [
            "mature",
            "afraid",
            "global",
            "mountains"
    ]
    print(message.chat.id)
    if message.chat.id ==-1001953753607 :
        for word in ban_words:
            if word in message.text.lower().replace(" ",""):
                await bot.send_message(message.chat.id,f"{message.from_user.first_name}, used bad words")
                Database().sql_insert_ban_table(message.from_user.id, message.chat.id)
                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=message.message_id
                )

async def filter_messages(message: types.Message):
    MATY = ["mature",
            "afraid",
            "global",
            "mountains"]
    if message.chat.id == -1001953753607:
        for i in MATY:
            if i in message.text.lower().replace(' ', ''):
                if Database().sql_select_ban_for_users(message.from_user.username, message.chat.id):
                    await message.reply(text=f' {message.from_user.first_name} отправил '
                                             f'запрещённое слово\n'
                                             f'Админы удалят {message.from_user.first_name}')
                Database().sql_insert_ban_table(message.from_user.username, message.chat.id)
                await bot.ban_chat_member(message.chat.id, message.from_user.id)

                break

async def yes_no(message: types.Message):
    if message.chat.id == -1001953753607:
        admin_ans = await check_user_is_admin(message)
        print(admin_ans)
        if admin_ans and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )
answer = "yes"
check_user_is_admin = bot




def register_handlers_chat_actions(dp: Dispatcher):
    dp.register_message_handler(secret_word, lambda word: "nefor" in word.text)
    dp.register_message_handler(filter_messages)
    dp.register_message_handler(yes_no)
    dp.register_message_handler(echo_ban)