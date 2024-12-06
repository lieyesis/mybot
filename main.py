import asyncio
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'Привет!{name}')


# @dp.message()
# async def echo_handler(message: types.Message):
#    txt = message.text
#     await message.answer('txt')

@dp.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(f'Ваш ID: {id}; Ваше имя: {name}; Ваш ник: {username}.')


@dp.message(Command("random"))
async def random_handler(message: types.Message):
    name = ["Евгений", "Антон", "Алекс"]
    randomname = random.choice(name)
    await message.answer(f"Вот рандомное имя из списка: {randomname}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
