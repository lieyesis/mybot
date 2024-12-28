from aiogram import Router, types
from aiogram.filters import Command
from bot_config import database
from pprint import pprint

menu_router = Router()

@menu_router.message(Command("menu"))
async def start_handler(message: types.Message):
    meal_list = database.get_meals_by_price()
    pprint(meal_list)
    for meal in meal_list:
        photo = meal['photo']
        txt = (f"Название: {meal['name']}\n"
               f"Цена: {meal['price']}"
               f"Рецепт: {meal['receipt']}\n"
               f"Категория: {meal['category']}")
        await message.answer_photo(
            photo =photo,
            caption = txt
        )

