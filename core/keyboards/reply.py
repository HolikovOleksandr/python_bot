from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder



reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Show geo', request_location=True)],
        [KeyboardButton(text='My contact', request_contact=True)],
        [KeyboardButton(text='Rate bot', request_poll=KeyboardButtonPollType())],
    ], 
    resize_keyboard=True, 
    one_time_keyboard=False, 
    input_field_placeholder='Do thomething interesting!', 
    selective=True,
)



def get_reply_keyboard():
    kb = ReplyKeyboardBuilder()

    kb.button(text='Button 1')
    kb.button(text='Button 2')
    kb.button(text='Button 3')
    kb.button(text='Button 4')
    kb.button(text='Button 5')
    kb.button(text='Button 6')

    kb.adjust(1, 2, 3)
    return kb.as_markup(
        resize_keyboard=True, 
        one_time_keyboard=True,
        input_field_placeholder='Do thomething interesting!'
    ) 
