from aiogram import Router, types
from aiogram.filters import Command
import random
from bot_config import database


unit = "som"
random_meal_router = Router()

@random_meal_router.message(Command("random_meal"))
async def start_handler(message: types.Message):
    meal_list = database.get_meals_by_price()
    random_meal = random.choice(meal_list)
    print(random_meal)
    photo = (f"{random_meal['photo']}")
    await message.answer_photo(photo= photo,
                               caption = f"{random_meal['name']}"
                                         f"\n{random_meal['category']}"
                                         f"\n{random_meal['price']}{unit}"
                                         f"\n{random_meal['receipt']}")
