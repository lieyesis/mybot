from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext
from bot_config import database
from aiogram.filters import Command
from buttons import kb_food, kb_clean, kb_yes_no, kb_yes_no_keyb


list_user=[]


review_router = Router()

class RestourantReview(StatesGroup):
    name = State()
    instagram_username = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()
    confirm = State()

@review_router.message(Command("stop"))
@review_router.message(F.text == "stop")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Survey stopped")


@review_router.callback_query(F.data == "review", default_state)
async def start(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id in list_user:
        await callback.message.answer("You have already left a review")
    else:
        await callback.message.answer("What is your name?")
        await state.set_state(RestourantReview.name)

@review_router.message(RestourantReview.name)
async def ask_instagram(message: types.Message, state: FSMContext):
    name = message.text
    if len(name) > 20 or len(name) < 3:
        await message.answer("Please enter a valid name")
        return
    await state.update_data(name=message.text)
    await message.answer(f"{message.text}, What is your Instagram username?")
    await state.set_state(RestourantReview.instagram_username)

@review_router.message(RestourantReview.instagram_username)
async def ask_visit_date(message: types.Message, state: FSMContext):
    await state.update_data(instagram_username=message.text)
    await message.answer(f"When did you visit our establishment (yyyy-mm-dd)?")
    await state.set_state(RestourantReview.visit_date)


@review_router.message(RestourantReview.visit_date)
async def ask_food_rating(message: types.Message, state: FSMContext):
    visit_date = message.text
    if (
            len(visit_date) != 10 or
            not (visit_date[:4].isdigit() and visit_date[5:7].isdigit() and visit_date[8:].isdigit()) or
            visit_date[4] != "-" or visit_date[7] != "-"
    ):
        await message.answer("Please enter a valid date in the format YYYY-MM-DD, for example, 2024-12-31.")
        return
    await state.update_data(visit_date=visit_date)

    await message.answer("How would you rate the food quality?", reply_markup=kb_food)
    await state.set_state(RestourantReview.food_rating)


@review_router.message(RestourantReview.food_rating)
async def ask_cleanliness_rating(message: types.Message, state: FSMContext):
    food = message.text
    if not food.isdigit():
        await message.answer("Please enter a numerical value")
        return
    food = int(food)
    if food < 1 or food > 5:
        await message.answer("Please enter a rating from 1 to 5")
        return

    await state.update_data(food_rating=message.text)
    await message.answer("How would you rate the cleanliness of the establishment?", reply_markup=kb_clean)
    await state.set_state(RestourantReview.cleanliness_rating)

@review_router.message(RestourantReview.cleanliness_rating)
async def ask_extra_comments(message: types.Message, state: FSMContext):
    clean = message.text
    if not clean.isdigit():
        await message.answer("Please enter a numerical value")
        return
    clean = int(clean)
    if clean < 1 or clean > 5:
        await message.answer("Please enter a rating from 1 to 5")
        return
    await state.update_data(cleanliness_rating=message.text)

    await message.answer("Do you have any additional comments or complaints?", reply_markup=kb_yes_no)
    list_user.append(message.from_user.id)
    await state.set_state(RestourantReview.extra_comments)

@review_router.callback_query(RestourantReview.extra_comments, F.data == "yes")
async def ask_for_comment(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Please leave your comment.")
    await state.set_state(RestourantReview.extra_comments)


@review_router.callback_query(RestourantReview.extra_comments, F.data == "no")
async def skip_comment(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    review = (
        f"Thank you for your review!\n"
        f"Name: {data['name']}\n"
        f"Instagram: {data['instagram_username']}\n"
        f"Food rating: {data['food_rating']}\n"
        f"Cleanliness rating: {data['cleanliness_rating']}\n"
        f"Additional comments: No comments"
    )

    await state.set_state(RestourantReview.confirm)
    await callback.message.answer("Would you like to save the review?", reply_markup=kb_yes_no_keyb)
    await callback.message.answer(review)
    await state.set_state(RestourantReview.confirm)


@review_router.message(RestourantReview.extra_comments)
async def finish_review(message: types.Message, state: FSMContext):
    list_user.append(message.from_user.id)
    data = await state.get_data()
    review = (
        f"Thank you for your review!\n"
        f"Name: {data['name']}\n"
        f"Instagram: {data['instagram_username']}\n"
        f"Visit date: {data['visit_date']}\n"
        f"Food rating: {data['food_rating']}\n"
        f"Cleanliness rating: {data['cleanliness_rating']}\n"
        f"Additional comments: {message.text}"
    )

    await message.answer(review)
    await message.answer("Would you like to save the review?", reply_markup=kb_yes_no_keyb)
    await state.set_state(RestourantReview.confirm)

@review_router.message(RestourantReview.confirm)
async def save_review(message: types.Message, state: FSMContext):
    if message.text == "yes":
        data = await state.get_data()
        print(data)
        database.save_survey(data)
        await message.answer("Review saved")
        await state.clear()
    else:
        await state.clear()
