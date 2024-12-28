from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext
from bot_config import database
from pprint import pprint

admin_router = Router()
admin_router.message.filter(F.from_user.id == 6573322342)
admin_router.callback_query.filter(F.from_user.id == 6573322342)


class Meal(StatesGroup):
    name = State()
    price = State()
    photo = State()
    receipt = State()
    category = State()


@admin_router.message(Command("stop"))
@admin_router.message(F.text == "stop")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Survey stopped")


@admin_router.message(Command("new_meal"), default_state)
async def name_meal(message: types.Message, state: FSMContext):
    await message.answer("Please enter the name of the dish")
    await state.set_state(Meal.name)


@admin_router.message(Meal.name)
async def price_meal(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Please enter the price of the dish")
    await state.set_state(Meal.price)


@admin_router.message(Meal.price)
async def meal_photo(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Please upload a photo of the dish")
    await state.set_state(Meal.photo)


@admin_router.message(Meal.photo)
async def set_receipt(message: types.Message, state: FSMContext):
    meal_photo = message.photo
    pprint(meal_photo)
    biggest_image = meal_photo[-1]
    biggest_image_id = biggest_image.file_id
    await state.update_data(photo=biggest_image_id)
    await message.answer("Please enter the recipe/description of the dish")
    await state.set_state(Meal.receipt)


@admin_router.message(Meal.receipt)
async def set_category(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Soups"),
                types.KeyboardButton(text="Main courses")
            ],
            [
                types.KeyboardButton(text="Hot dishes"),
                types.KeyboardButton(text="Drinks")
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder="Select a category"
    )
    await state.update_data(receipt=message.text)
    await message.answer("Please select a category for your dish", reply_markup=kb)
    await state.set_state(Meal.category)


@admin_router.message(Meal.category)
async def create_new_dish(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    data = await state.get_data()
    print(data)
    database.save_meal(data)
    await message.answer("Dish saved")
    await state.clear()
