from aiogram import Router,types
from aiogram.filters import Command
import random

random_router = Router()


@random_router.message(Command("random"))
async def random_handler(message: types.Message):
    name = ["печеньки в виде новогодней атрибутики", "печеньки с начинкой", "печнька с предсказанием предстоящего года"]
    random_router = random.choice(name)
    await message.answer(f"Вот рандомный рецепт из новогоднего списка печенек: {random_router}")