from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text= 'Купить\U0001F4B3')],
        [KeyboardButton(text= 'Регистрация')],
        [
            KeyboardButton(text= 'Информация о боте\U0001F4A1'),
            KeyboardButton(text= 'Рассчитать норму калорий\U0001F4D2')
        ]
    ], resize_keyboard = True
)


inbutkeyb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= 'Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text= 'Формулы расчёта', callback_data='formulas')
        ]
    ], resize_keyboard = True
)


buying_kb = InlineKeyboardMarkup(
    inline_keyboard= [
        [KeyboardButton(text= 'Product 1', callback_data= 'product_buying'), KeyboardButton(text= 'Product 2', callback_data= 'product_buying')],
        [KeyboardButton(text= 'Product 3', callback_data= 'product_buying'), KeyboardButton(text= 'Product 4', callback_data= 'product_buying')]
    ], resize_keyboard = True
)
