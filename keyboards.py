from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎲 Случайный фильм"), KeyboardButton(text="💖 Случайное из избранного")]
    ],
    resize_keyboard=True
)
