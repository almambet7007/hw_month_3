from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import  bot

async  def secret_word(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Список пользователей",
        callback_data="list_of_users"
    )
    markup.add(button_call_1)
    if message.chat.id !=-1001953753607:
        await message.reply("ok,BOSS",
                            reply_markup=markup)


async def echo_ban(message: types.Message):
    ban_words = ["bitch", "damn", "fuck"]
    print(message.chat.id)
    print(type(message.chat.id))
    if message.chat.id == -1001953753607:
        for word in ban_words:
            if word in message.text.lower().replace("",''):
                await bot.send_message(message.chat.id,
                                       "don't use this words!")
                await  bot.delete_message(
                    chat_id=message.chat.id,
                    message_id = message.message_id
                )


def register_handlers_chat_actions(dp: Dispatcher):
    dp.register_message_handler(secret_word, lambda word: "one piece" in word.text)
    dp.register_message_handler(echo_ban)