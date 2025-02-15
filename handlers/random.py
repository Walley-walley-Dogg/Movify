from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from api import get_random_movie

router = Router()

@router.message(lambda msg: msg.text == "🎲 Случайный фильм")
async def send_random_movie(message: Message):
    movie = get_random_movie()
    
    if movie:
        text = (
            f"🎬 *Название:* {movie['title']}\n"
            f"📅 *Год:* {movie['year']}\n"
            f"🌍 *Страна:* {movie['countries']}\n"
            f"🎭 *Жанры:* {movie['genres']}\n"
            f"⭐ *Рейтинги:* {movie['ratings']}\n"
            f"🔞 *Возрастное ограничение:* {movie['ageRating']}"
        )
        if movie.get("poster"):
            await message.answer_photo(photo=movie["poster"], caption=text, parse_mode="Markdown")
        else:
            await message.answer(text, parse_mode="Markdown")
        
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text="⭐ Добавить в избранное",
                callback_data=f"fav_{movie['title']}"
            )]
        ])
        await message.answer("Хотите добавить этот фильм в избранное?", reply_markup=keyboard)
    else:
        await message.answer("❌ Не удалось получить фильм. Попробуй ещё раз!")