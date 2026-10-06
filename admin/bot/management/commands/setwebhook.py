import asyncio
from aiogram import Bot
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        async def main():
            bot = Bot(settings.BOT_TOKEN)
            await bot.set_webhook(
                settings.WEBHOOK_URL,
                secret_token=settings.WEBHOOK_SECRET,
                drop_pending_updates=True,
            )
            await bot.session.close()
        asyncio.run(main())
        self.stdout.write("Webhook o'rnatildi")