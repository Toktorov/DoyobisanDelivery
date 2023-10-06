from django.contrib import admin

from apps.order.models import Order, OrderItem

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'display_items', 'created')

    def display_items(self, obj):
        items = obj.items.all()  # Получаем все связанные товары
        item_names = ", ".join([item.title for item in items])  # Формируем список имен товаров
        return item_names
    display_items.short_description = 'Items'

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total', 'order')