from aiogram import Bot, Dispatcher
from config import TOKEN

from handlers import random_favorite, start, random, favorite_add, favorite_delete

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(random.router)
dp.include_router(random_favorite.router)
dp.include_router(favorite_add.router)
dp.include_router(favorite_delete.router)