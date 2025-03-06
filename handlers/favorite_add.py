from aiogram import Router
from aiogram.types import CallbackQuery
from database import add_favorite

router = Router()

@router.callback_query(lambda c: c.data.startswith("fav_"))
async def add_to_favorites(callback: CallbackQuery):
    try:
        _, movie_id, movie_title, movie_year, movie_country, movie_poster, movie_genres, movie_ratings = callback.data.split("_", 7)
    except ValueError:
        await callback.answer("Ошибка обработки данных.")
        return

    user_id = callback.from_user.id
    movie = {
        "id": movie_id,
        "title": movie_title,
        "year": movie_year,
        "countries": movie_country,
        "poster": movie_poster if movie_poster != "None" else None,
        "genres": movie_genres,
        "rating": movie_ratings
    }

    success = add_favorite(user_id, movie)

    if success:
        await callback.answer("✅ Фильм добавлен в избранное!")
    else:
        await callback.answer("⚠️ Этот фильм уже есть в избранном!")