from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *

formula1 = ('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5; \n'
           ' для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')

initiate_db()
db = get_all_products()

api = 'key'
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
button3 = KeyboardButton(text = 'Купить')
kb.row(button, button2)
kb.add(button3)

kb1 = InlineKeyboardMarkup()
butt1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
butt2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb1.row(butt1, butt2)

kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')]
    ]
)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)

@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer('Информация о бот')

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = kb1)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(formula1)
    await call.answer()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age = int(message.text))
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = int(message.text))
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = int(message.text))
    data = await state.get_data()
    calories = data['weight'] * 10 + data['growth'] * 6.25 - 5 * data['age'] + 5
    await message.answer(f'Ваша норма калорий {calories}')
    await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in db:
        await message.answer(f'Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}')
        with open(f'lec{i[0]}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберете продукт для покупки: ', reply_markup = kb2)

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)