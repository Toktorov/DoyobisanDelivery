from django.contrib import admin

from apps.telegram.models import TelegramUser

# Register your models here.
@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'user_id', 'created')
    search_fields = ('username', 'first_name', 'last_name', 'user_id', 'created')