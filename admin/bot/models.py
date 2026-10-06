from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(
        primary_key=True,
        verbose_name="Telegram ID",
    )

    username = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )

    first_name = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )

    last_name = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
        default="",
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.telegram_id} - {self.username}"




class Session(models.Model):
    user = models.OneToOneField(
        TelegramUser,
        on_delete=models.CASCADE,
        related_name="session",
    )

    secret_key = models.CharField(
        max_length=64,
        unique=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    last_login = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = "sessions"

    def __str__(self):
        return f"Session: {self.user.telegram_id}"