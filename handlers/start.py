from config import bot
from aiogram import  types, Dispatcher
from database.sql_commands import  Database
from aiogram.types import ParseMode as Parse, InlineKeyboardButton as Button, InlineKeyboardMarkup as Markup

async def start_button_game(message: types.Message):
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    Database().sql_insert_users(username=username,
                                first_name=first_name,
                                last_name=last_name)
    await message.reply(text=f'Hello {message.from_user.username}, how are you?')


async def victory_1(message: types.Message):
    mark = Markup()
    button_1 = Button(
        "Next Victory",
        callback_data="button_1"
    )
    mark.add(button_1)

    question = "Чему равно 2+2*2?"
    option = [
        "8",
        "16",
        "4",
        "6"
    ]
    await bot.send_poll(
        chat_id= message.chat.id,
        question=question,
        options=option,
        is_anonymous=False,
        type="quiz",
        correct_option_id=3,
        explanation="if you don't ask, you must learn math",
        explanation_parse_mode=Parse.MARKDOWN,
        reply_markup=mark
    )

async def victory_2(call: types.CallbackQuery):

    question = "Чему равно 3+3*3?"
    option = [
        "9",
        "11",
        "31",
        "44"
    ]
    await bot.send_poll(
        chat_id= call.message.chat.id,
        question=question,
        options=option,
        is_anonymous=False,
        type="quiz",
        correct_option_id=1,
        explanation="if you don't ask, you must learn math",
        explanation_parse_mode=Parse.MARKDOWN,

    )



def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_button_game, commands=["start"])
    dp.register_message_handler(victory_1, commands=["play"])
    dp.register_callback_query_handler(victory_2,lambda call: call.data == "button_1")