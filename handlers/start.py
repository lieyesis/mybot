from aiogram import Router,types
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'Привет {name}! Я твой новый помощник в создании вкусных блюд!')