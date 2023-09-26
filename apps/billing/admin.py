from django.contrib import admin

from apps.billing.models import Billing, BillingProduct

# Register your models here.
@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('billing_receipt_type', 'total_price', 'payment_code', 'created')

@admin.register(BillingProduct)
class BillingProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')