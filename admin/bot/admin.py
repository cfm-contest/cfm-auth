from django.contrib import admin

from .models import TelegramUser, Session


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = (
        "telegram_id",
        "username",
        "first_name",
        "last_name",
        "phone",
        "is_active",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "telegram_id",
        "username",
        "first_name",
        "last_name",
        "phone",
    )

    list_filter = (
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-updated_at",
    )


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "secret_key",
        "created_at",
        "last_login",
    )

    search_fields = (
        "user__telegram_id",
        "user__username",
    )

    readonly_fields = (
        "created_at",
        "last_login",
    )

    ordering = (
        "-last_login",
    )