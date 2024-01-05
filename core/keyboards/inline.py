from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder



inline_buttons = InlineKeyboardMarkup(inline_keyboard=[
	[InlineKeyboardButton(text='Macbook Air 13" M1 2020', callback_data='apple_air_13"_m1_2020')],
	[InlineKeyboardButton(text='Macbook Pro 14" M1 2021', callback_data='apple_pro_14"_m1_2021')],
	[InlineKeyboardButton(text='Macbook Pro 16" I7 2019',callback_data='apple_pro_16"_i7_2019')],
])


def get_inline_keyboard():
	kb = InlineKeyboardBuilder()

	kb.button(text='Macbook Air 13" M1 2020', callback_data='apple_air_13"_m1_2020')
	kb.button(text='Macbook Pro 14" M1 2021', callback_data='apple_pro_14"_m1_2021')
	kb.button(text='Macbook Pro 16" I7 2019', callback_data='apple_pro_16"_i7_2019')

	return kb.as_markup()



