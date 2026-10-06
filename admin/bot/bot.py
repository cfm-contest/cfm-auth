# bot/bot.py
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from django.conf import settings

bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(m: types.Message):
    await m.answer(f"Salom, {m.from_user.first_name}!")