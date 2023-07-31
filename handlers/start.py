import sqlite3

from config import bot
from aiogram import types,Dispatcher
from database.sql_commands import Database
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from const import HELP_TEXT
from keyboards import start_keyboard
from scraper.news_scraper import NewScraper
from scraper.lukizm_scraper import LukScraper
from scraper.asyn_limon import AsyncLimonScraper

async def start_button(message: types.Message):
    telegram_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    Database().sql_insert_user(telegram_id=telegram_id,
                               username=username,
                               first_name=first_name,
                               last_name=last_name)
    await message.reply(text=f"hello {message.from_user.username}",
                        reply_markup=start_keyboard.start_markup)


async def help_button(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=HELP_TEXT)

quiz_id = None
async def quiz_1(message: types.Message):
    global quiz_id
    quiz_id = "quiz_1"
    markup = InlineKeyboardMarkup()        #
    button_call_1 = InlineKeyboardButton(  #это код кнопки для перехода
        "next victory",                    #к следующей викторине
        callback_data= "button_call_1"     #
    )
    markup.add(button_call_1)
    question = "Who invented Python"
    option = [
        "alma",
        "jaka",
        "Linus Torwalds",
        "Guido Van Rossum"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=option,
        is_anonymous=False,
        type="quiz",
        correct_option_id= 3,
        explanation="this is so easy",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_2(call: types.CallbackQuery):
    global quiz_id
    quiz_id = "quiz_2"
    question = "Who invented Linux?"
    option = [
        "aska",
        "baha",
        "Linus Torwalds",
        "Guido Van Rossum"
    ]
    await  bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=option,
        is_anonymous=False,
        type="quiz",
        correct_option_id= 2,
        explanation="this is so easy",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


async def answer_in_poll(poll_answer: types.PollAnswer):
      Database().sql_answer_query(id_user=poll_answer.user.id,
                                username=poll_answer.user.username,
                                quiz=quiz_id,
                                quiz_option=poll_answer.option_ids[0])


async def call_scraper(message: types.Message):
    links = NewScraper().parse_data()
    for link in links[:6]:
        await message.reply(text=f"https://www.prnewswire.com{link}")



async def lukizm_scraper(message: types.Message):
    links_luk = LukScraper().get_data()
    for link_luk in links_luk[:5]:
        await message.reply(text=f"https://mangalib.me{link_luk}")
     # try:
     #  if links_luk != []:
     #       print("hello")
     #  else:
     #      await message.reply(text=f"https://mangalib.me{link_luk}")
     # except TypeError as S:
     #     print("error in ", S)
def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=["start"])
    dp.register_message_handler(call_scraper, commands=["get_latest_news"])
    dp.register_message_handler(lukizm_scraper, commands=["lukizm"])
    dp.register_message_handler(help_button, commands=["help"])
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_poll_answer_handler(answer_in_poll)
