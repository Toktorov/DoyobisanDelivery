from django.shortcuts import render, redirect
from django.db import transaction
from django.db.models import F

from apps.settings.models import Setting
from apps.carts.models import Cart, CartItem
from apps.billing.models import Billing, BillingProduct

# Create your views here.
def confirm(request, address, phone, payment_code):
    setting = Setting.objects.latest('id')
    result = {'address':address, 'phone':phone, 'payment_code':payment_code}
    return render(request, 'billing/confirm.html', locals())

def create_billing_from_cart(request):
    user_cart = request.POST.get('user_cart')
    billing_receipt_type = request.POST.get('billing_receipt_type')
    print(request.POST)
    print(billing_receipt_type)
    total_price = request.POST.get('total_price')
    print(total_price)
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    with transaction.atomic():
        # Создаем объект Billing
        billing = Billing.objects.create(
            billing_receipt_type=billing_receipt_type,
            total_price=total_price,
            address=address,
            phone=phone
            # Другие поля Billing могут быть заполнены здесь
        )
        # Получаем или создаем корзину для текущей сессии
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        print("MIDDLE")

        # Получаем товары из корзины пользователя
        cart = Cart.objects.get_or_create(session_key=session_key)
        print(cart)
        # Создаем BillingProduct для каждого товара в корзине
        
        cart_products = CartItem.objects.filter(cart__session_key=session_key)
        print(cart_products)
        for cart_item in cart_products:
            print(cart_item)
            BillingProduct.objects.create(
                billing=billing,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.total
            )

        # Опционально: Очищаем корзину пользователя после создания заказа
        # cart.clear()

        return redirect('confirm', billing.address, billing.phone, billing.payment_code)