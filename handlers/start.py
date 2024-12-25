from aiogram import Router, F, types
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
                types.InlineKeyboardButton(text='о нас', callback_data='about_us')
            ],
            [
                types.InlineKeyboardButton(text='оставьте отзыв', callback_data='restourantreview')
            ],
        ]
    )
    await message.answer(f'Привет {name}! Я твой новый помощник в создании вкусных блюд!', reply_markup=kb)

@start_router.callback_query(F.data == "about_us")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('наша инфа')



