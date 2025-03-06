from aiogram import Router
from aiogram.types import Message
from database import get_random_favorite

router = Router()

@router.message(lambda msg: msg.text == "🎲 Случайное из избранного")
async def send_random_favorite(message: Message):
    user_id = message.from_user.id
    movie = get_random_favorite(user_id)

    if movie:
        movie_id, title, year, country, poster, genres, ratings = movie
        text = (
            f"🎬 *Название:* {title}\n"
            f"📅 *Год:* {year}\n"
            f"🌍 *Страна:* {country}\n"
            f"🎭 *Жанры:* {genres}\n"
            f"⭐ *Рейтинги:* {ratings}"
        )
        if poster:
            await message.answer_photo(photo=poster, caption=text, parse_mode="Markdown")
        else:
            await message.answer(text, parse_mode="Markdown")
    else:
        await message.answer("❌ У вас пока нет избранных фильмов!")