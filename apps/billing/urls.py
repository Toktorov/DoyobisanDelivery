from django.urls import path 

from apps.billing.views import create_billing_from_cart

urlpatterns = [
    path('create/', create_billing_from_cart, name="create_billing")
]