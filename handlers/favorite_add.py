from aiogram import Router
from aiogram.types import CallbackQuery
from database import cursor, conn

router = Router()

@router.callback_query(lambda c: c.data.startswith("fav_"))
async def add_to_favorites(callback: CallbackQuery):
    movie_title = callback.data[4:]
    user_id = callback.from_user.id

    cursor.execute("SELECT * FROM favorites WHERE user_id = ? AND movie_title = ?", (user_id, movie_title))
    if cursor.fetchone() is None:
        cursor.execute(
            "INSERT INTO favorites (user_id, movie_title) VALUES (?, ?)",
            (user_id, movie_title)
        )
        conn.commit()
        await callback.answer("✅ Фильм добавлен в избранное!")
    else:
        await callback.answer("⚠️ Этот фильм уже в избранном!")