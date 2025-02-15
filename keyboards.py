from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎲 Случайный фильм"), KeyboardButton(text="⭐ Избранные")]
    ],
    resize_keyboard=True
)
