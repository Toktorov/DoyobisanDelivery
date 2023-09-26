from django.shortcuts import render
from django.db import transaction

from apps.carts.models import Cart, CartItem
from apps.billing.models import Billing, BillingProduct

# Create your views here.
def create_billing_from_cart(user_cart, billing_receipt_type, total_price):
    try:
        with transaction.atomic():
            # Создаем объект Billing
            billing = Billing.objects.create(
                billing_receipt_type=billing_receipt_type,
                total_price=total_price,
                # Другие поля Billing могут быть заполнены здесь
            )

            # Получаем товары из корзины пользователя
            cart_items = CartItem.objects.filter(cart=user_cart)

            # Создаем BillingProduct для каждого товара в корзине
            for cart_item in cart_items:
                BillingProduct.objects.create(
                    billing=billing,
                    product=cart_item.product,
                    quantity=cart_item.quantity
                )

            # Опционально: Очищаем корзину пользователя после создания заказа
            user_cart.items.clear()

            return billing
    except Exception as e:
        # Обработка ошибок, если не удается создать биллинг
        # Например, можно записать лог ошибки
        print(f"Error creating billing: {e}")
        return None