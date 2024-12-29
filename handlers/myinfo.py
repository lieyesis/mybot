from aiogram import Router,types
from aiogram.filters import Command


myinfo_router = Router()


@myinfo_router.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(f'Ваш ID: {id}; Ваше имя: {name}; Ваш ник: {username}.')