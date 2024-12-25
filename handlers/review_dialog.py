from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

class restourantreview(StatesGroup):
    Name = State()
    Food_rating = State()
    Cleanliness_rating = State()
    Extra_comments = State()

restourantreview_Router = Router()

@restourantreview_Router.callback_query(F.data == "restourantreview")
async def start_opros(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('как ваc зовут?')
    await state.set_state(restourantreview.Name)

@restourantreview_Router.message(restourantreview.Name)
async def srart_opros(message: types.Message, state: FSMContext):
    await message.answer('Как оцениваете качество еды?')
    await state.set_state(restourantreview.Food_rating)

@restourantreview_Router.message(restourantreview.Food_rating)
async def srart_opros(message: types.Message, state: FSMContext):
    food_rating = message.text
    if not food_rating.isdigit():
        await message.answer('Пожалуйста юзайте онли цифры!')
        return
    food_rating = int(food_rating)
    if food_rating < 0 and food_rating > 5:
        await message.answer('Можно поставить оценку от 1го до 5ти')
        return
    await message.answer('Как оцениваете чистоту заведения?')
    await state.set_state(restourantreview.Cleanliness_rating)

@restourantreview_Router.message(restourantreview.Cleanliness_rating)
async def srart_opros(message: types.Message, state: FSMContext):
    cleanliness_rating = message.text
    if not cleanliness_rating.isdigit():
        await message.answer('Пожалуйста юзайте только цифры!')
        return
    cleanliness_rating = int(cleanliness_rating)
    if cleanliness_rating < 0 and cleanliness_rating > 5:
        await message.answer('Можно поставить оценку от 1го до 5ти')
        return
    await message.answer('Оствьте свои идеи для улучшения нашего сериса или жалобу')
    await state.set_state(restourantreview.Extra_comments)

@restourantreview_Router.message(restourantreview.Extra_comments)
async def srart_opros(message: types.Message, state: FSMContext):
    await message.answer('Спасибо за пройденный опрос')

    await state.clear()

