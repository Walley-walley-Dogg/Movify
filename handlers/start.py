from aiogram import Router
from aiogram.types import Message
from keyboards import menu_keyboard

router = Router()

@router.message(lambda msg: msg.text == "/start")
async def send_welcome(message: Message):
    text = (
        "👋 Привет! Я бот для поиска случайных фильмов.\n\n"
        "📌 Используйте кнопки ниже для взаимодействия."
    )
    await message.answer(text, reply_markup=menu_keyboard)
