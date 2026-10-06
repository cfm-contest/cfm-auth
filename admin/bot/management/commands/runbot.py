import asyncio
from django.core.management.base import BaseCommand
from bot.bot import bot, dp


class Command(BaseCommand):
    help = "Botni polling rejimida ishga tushirish"

    def handle(self, *args, **options):
        async def main():
            await bot.delete_webhook(drop_pending_updates=True)
            await dp.start_polling(bot)

        asyncio.run(main())