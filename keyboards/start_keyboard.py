from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton


help_button = KeyboardButton("/help")
quiz_button = KeyboardButton("/quiz")

start_markup = ReplyKeyboardMarkup(resize_keyboard= True,one_time_keyboard=True)

start_markup.row(
    help_button,
    quiz_button

)