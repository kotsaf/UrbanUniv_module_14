from art import tprint
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import *
from crud_functions import *

api = '7812004269:AAGnGigM_tZonbzCTlqyeef0g89MBm6xQQg'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
initiate_db()

@dp.message_handler(text= 'Рассчитать норму калорий\U0001F4D2')
async def info(message):
    await message.answer('Выберите опцию: ', reply_markup = inbutkeyb)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands= ['start'])
async def start(message):
    await message.answer(f'Привет, {message.from_user.username}!', reply_markup = start_menu)

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()

@dp.message_handler(text='Информация о боте\U0001F4A1')
async def info(message):
    await message.answer('Я бот-помощник! Помогу расчитать твою дневную норму калорий \U0001F970')

@dp.message_handler(text='Купить\U0001F4B3')
async def get_buying_list(message):
    for index, product in enumerate(get_all_products()):
        await message.answer(f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}")
        with open(f'D:\Projects\BOT\домашки\images/image{index + 1}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукцию:', reply_markup=buying_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!\U0001F970')
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(
        f'Ваша дневная норма калорий: '
        f'{10 * int(data["weight"]) + 6.25 * int(data["growth"]) + 5 * int(data["age"]) + 5} \U00002764',
    reply_markup = start_menu)
    await state.finish()

@dp.message_handler()                          # реагирует на все
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    tprint('<<botik>>', 'bulbhead')
    executor.start_polling(dp, skip_updates=True)