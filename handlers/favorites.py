from aiogram import Router
from aiogram.types import Message
from database import get_favorites

router = Router()

@router.message(lambda msg: msg.text == "⭐ Избранные")
async def show_favorites(message: Message):
    user_id = message.from_user.id
    movies = get_favorites(user_id)

    if movies:
        text = "⭐ *Ваши избранные фильмы:*\n\n" + "\n".join(f"🎬 {m[0]}" for m in movies)
    else:
        text = "😔 У вас пока нет избранных фильмов."
    
    await message.answer(text, parse_mode="Markdown")
