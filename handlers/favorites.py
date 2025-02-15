import urllib.parse
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database import cursor

router = Router()

@router.message(lambda msg: msg.text == "⭐ Избранные")
async def show_favorites(message: Message):
    user_id = message.from_user.id
    cursor.execute("SELECT movie_title FROM favorites WHERE user_id = ?", (user_id,))
    movies = cursor.fetchall()

    if movies:
        text = "⭐ *Ваши избранные фильмы:*\n\n"
        keyboard_buttons = []
        for m in movies:
            movie_title = m[0]
            text += f"• {movie_title}\n"
            # Кодируем название фильма для callback_data
            encoded_title = urllib.parse.quote(movie_title)
            btn = InlineKeyboardButton(text="❌ Удалить", callback_data=f"del_{encoded_title}")
            keyboard_buttons.append([btn])
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
        await message.answer(text, parse_mode="Markdown", reply_markup=keyboard)
    else:
        await message.answer("😔 У вас пока нет избранных фильмов!")