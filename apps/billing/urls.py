from django.urls import path 

from apps.billing.views import create_billing_from_cart, confirm

urlpatterns = [
    path('create/', create_billing_from_cart, name="create_billing"),
    path('confirm/<str:address>/<str:phone>/<str:payment_code>/', confirm, name='confirm'),
]