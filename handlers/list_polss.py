from aiogram import Dispatcher, types
from  aiogram.dispatcher import FSMContext
from  aiogram.dispatcher.filters import  Text
from aiogram.dispatcher.filters.state import  State, StatesGroup
from aiogram.types import ContentType
from aiogram.types import  InlineKeyboardButton,InlineKeyboardMarkup
from config import bot
from database.sql_commands import  Database
from handlers.fsm_form import FormStates
from aiogram.types import CallbackQuery

class FormStates_2(StatesGroup):
    variant_poll = State()

async def list_user_poll(call: types.CallbackQuery):
    variant_polls = Database().sql_select_user_form()
    send_message = ""
    for variant_poll in variant_polls:
        send_message += f'id: {variant_poll[0]}\n\
                        nickname: {variant_poll[1]}\n\
                        age:  {variant_poll[2]}\n\
                        bio :  {variant_poll[3]}\n\
                        gender :  {variant_poll[4]}\n\
                        idea :  {variant_poll[5]}\n\
                        problems :  {variant_poll[6]}\n\
                        place :  {variant_poll[7]}\n\
                        photo :  {variant_poll[8]}\n\n'
    await bot.send_message(call.message.chat.id,send_message)
    await bot.send_message(call.message.chat.id,"выберите опросник по ID")
    await FormStates_2.variant_poll.set()

async def load_variant_poll(message: types.Message,
                            state: FSMContext):
    async with state.proxy() as data:
        data["user_variant_poll"] = message.text

    variant_poll = Database().sql_select_user_form_by_id(int(data["user_variant_poll"]))

    if variant_poll:
        message_result =f'идея: {variant_poll[0][1]}\n'\
                     f'проблемы: {variant_poll[0][2]}\n'\
                     f'оценка: {variant_poll[0][3]}\n'\
                     f'пользователь: {variant_poll[0][6]}\n'\
                     f'имя: {variant_poll[0][7]}\n'\
                     f'фамилия: {variant_poll[0][8]}\n'\
                     f'id пользователя: {variant_poll[0][5]}'

        markup = InlineKeyboardMarkup()
        button_call_for_poll = InlineKeyboardButton(
            "Список профилей",
            callback_data="list_of_poll_user"
        )
        markup.add(button_call_for_poll)
        await message.reply(message_result, reply_markup=markup)

    else:
        await bot.send_message(message.chat.id, 'Нечего не найдено!')
def register_handler_list_poll(dp: Dispatcher):
    dp.register_message_handler(load_variant_poll, lambda word: "find" in word.text,state=FormStates_2.variant_poll,content_types=["text"])
    # dp.register_message_handler(load_variant_poll,commands=["find"],state=FormStates_2.variant_poll,content_types=["text"])

