from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

api = 'key'
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()

@dp.message_handler(text=['Calories'])
async def set_age(message):
    await message.answer('Введите свой возраст: ')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_gender(message, state):
    await state.update_data(age = int(message.text))
    await message.answer('Введите свой пол: М или W')
    await UserState.gender.set()

@dp.message_handler(state=UserState.gender)
async def set_growth(message, state):
    await state.update_data(gender = message.text)
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
    if data['gender'] == 'M':
        calories = data['weight'] * 10 + data['growth'] * 6.25 - 5 * data['age'] + 5
    else:
        calories = data['weight'] * 10 + data['growth'] * 6.25 - 5 * data['age'] - 161
    await message.answer(f'Ваша дневная норма составляет {calories} ккал')
    await state.finish()

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

    """для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161."""