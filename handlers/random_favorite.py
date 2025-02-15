import random
from aiogram import Router
from aiogram.types import Message
from database import cursor

router = Router()

@router.message(lambda msg: msg.text == "💖 Случайное из избранного")
async def send_random_favorite(message: Message):
    user_id = message.from_user.id
    cursor.execute("SELECT movie_title, movie_year, movie_country, movie_poster, movie_genres, movie_ratings FROM favorites WHERE user_id = ?", (user_id,))
    movies = cursor.fetchall()

    if not movies:
        await message.answer("😔 У вас пока нет избранных фильмов.")
        return

    movie = random.choice(movies) 
    title, year, country, poster, genres, ratings = movie

    text = (
        f"🎬 *Название:* {title}\n"
        f"📅 *Год:* {year}\n"
        f"🌍 *Страна:* {country}\n"
        f"🎭 *Жанр:* {genres}\n"
        f"⭐ *Рейтинги:* {ratings}"
    )

    if poster:
        await message.answer_photo(photo=poster, caption=text, parse_mode="Markdown")
    else:
        await message.answer(text, parse_mode="Markdown")