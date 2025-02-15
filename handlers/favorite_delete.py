import urllib.parse
from aiogram import Router
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from database import cursor, conn

router = Router()

# Первый шаг: запрос подтверждения удаления
@router.callback_query(lambda c: c.data.startswith("del_"))
async def request_delete_favorite(callback: CallbackQuery):
    # Извлекаем и декодируем название фильма
    encoded_title = callback.data[4:]
    movie_title = urllib.parse.unquote(encoded_title)
    
    # Формируем inline-клавиатуру с кнопками "Да" и "Нет"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data=f"confirm_del_{encoded_title}"),
            InlineKeyboardButton(text="Нет", callback_data="cancel")
        ]
    ])
    await callback.message.edit_text(
        f"Вы уверены, что хотите удалить фильм *{movie_title}* из избранного?",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

# Второй шаг: обработка подтверждения удаления
@router.callback_query(lambda c: c.data.startswith("confirm_del_"))
async def confirm_delete_favorite(callback: CallbackQuery):
    encoded_title = callback.data[len("confirm_del_"):]
    movie_title = urllib.parse.unquote(encoded_title)
    user_id = callback.from_user.id

    cursor.execute("SELECT * FROM favorites WHERE user_id = ? AND movie_title = ?", (user_id, movie_title))
    if cursor.fetchone() is not None:
        cursor.execute("DELETE FROM favorites WHERE user_id = ? AND movie_title = ?", (user_id, movie_title))
        conn.commit()
        await callback.message.edit_text(f"✅ Фильм *{movie_title}* удалён из избранного!", parse_mode="Markdown")
        await callback.answer("Фильм удалён.")
    else:
        await callback.answer("⚠️ Фильм не найден в избранном.", show_alert=True)

# Отмена удаления
@router.callback_query(lambda c: c.data == "cancel")
async def cancel_delete(callback: CallbackQuery):
    await callback.answer("Удаление отменено.")
    # Убираем inline-клавиатуру, возвращая исходное сообщение
    await callback.message.edit_reply_markup(reply_markup=None)