from aiogram.filters import Command
from aiogram import Router, types, F


start_router = Router()

list_id = []

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    if message.from_user.id not in list_id:
        list_id.append(message.from_user.id)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text = "review", callback_data = "review")]
        ]
    )
    await message.answer(f"Hello {name},"
                         f"\nMy commands:"
                         f"\n/start - start working with bot"
                         f"\n/random_meal - random meal"
                         f"\n/menu - list of meals", reply_markup=kb)

