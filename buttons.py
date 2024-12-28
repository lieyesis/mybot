from aiogram import types


kb_food = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="1"),
                types.KeyboardButton(text="2"),
                types.KeyboardButton(text="3"),
                types.KeyboardButton(text="4"),
                types.KeyboardButton(text="5"),
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder="Оцените еду"
    )


kb_clean = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="1"),
                types.KeyboardButton(text="2"),
                types.KeyboardButton(text="3"),
                types.KeyboardButton(text="4"),
                types.KeyboardButton(text="5"),
            ],
        ],
        resize_keyboard = True,
        input_field_placeholder = "Оцените чистоту"
    )

kb_yes_no = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Да", callback_data="yes"),
                types.InlineKeyboardButton(text="Нет", callback_data="no")
            ],
        ]
    )


kb_yes_no_keyb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="да"),
                types.KeyboardButton(text="нет"),
            ],
        ],
    )