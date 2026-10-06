# bot/api.py
from aiogram.types import Update
from django.conf import settings
from django_bolt import BoltAPI
from django_bolt.exceptions import HTTPException

from .bot import bot, dp

api = BoltAPI()


@api.post("/tg/webhook")
async def webhook(request):
    headers = {k.lower(): v for k, v in request.get("headers", {}).items()}
    if headers.get("x-telegram-bot-api-secret-token") != settings.WEBHOOK_SECRET:
        raise HTTPException(status_code=403, detail="Forbidden")

    update = Update.model_validate_json(request.get("body", b""), context={"bot": bot})
    await dp.feed_update(bot, update)
    return {"ok": True}