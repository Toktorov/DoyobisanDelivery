from django.contrib import admin

from apps.billing.models import Billing, BillingProduct

# Register your models here.
class ProductTabularInline(admin.TabularInline):
    model = BillingProduct
    extra = 0

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'address', 'phone', 'billing_receipt_type', 'payment_code', 'created', 'status')
    inlines = [ProductTabularInline]

@admin.register(BillingProduct)
class BillingProductAdmin(admin.ModelAdmin):
    list_display = ('billing', 'product', 'quantity', 'price', 'status')