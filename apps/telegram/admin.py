from django.contrib import admin

from apps.telegram.models import TelegramUser, BillingDelivery, BillingDeliveryHistory

# Register your models here.
@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'user_id', 'user_role', 'created')
    search_fields = ('username', 'first_name', 'last_name', 'user_id', 'user_role', 'created')

@admin.register(BillingDelivery)
class BillingDeliveryAdmin(admin.ModelAdmin):
    list_display = ('billing', 'telegram_user', 'delivery', 'created')

@admin.register(BillingDeliveryHistory)
class BillingDeliveryHistoryAdmin(admin.ModelAdmin):
    list_display = ('delivery', 'message', 'created')