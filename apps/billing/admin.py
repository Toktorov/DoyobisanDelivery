from django.contrib import admin
from rangefilter.filter import DateRangeFilter
from datetime import date, timedelta
from django.utils.translation import gettext as _


from apps.billing.models import Billing, BillingProduct

# Register your models here.
class CustomDateFieldListFilter(admin.DateFieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.title = _('Дата')
        self.links = (
            (_('Сегодня'), {
                self.lookup_kwarg_since: str(date.today()),
            }),
            (_('Вчера'), {
                self.lookup_kwarg_since: str(date.today() - timedelta(days=1)),
                self.lookup_kwarg_until: str(date.today() - timedelta(days=1)),
            }),
            (_('Последние 7 дней'), {
                self.lookup_kwarg_since: str(date.today() - timedelta(days=7)),
            }),
            (_('Последние 30 дней'), {
                self.lookup_kwarg_since: str(date.today() - timedelta(days=30)),
            }),
        )

class ProductTabularInline(admin.TabularInline):
    model = BillingProduct
    extra = 0

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'address', 'payment_method', 'phone', 'billing_receipt_type', 'payment_code', 'created', 'status')
    search_fields = ('id', 'total_price', 'address', 'payment_method', 'phone', 'billing_receipt_type', 'payment_code', 'created', 'status')
    inlines = [ProductTabularInline]
    list_filter = (('created', DateRangeFilter), ('created', CustomDateFieldListFilter),)  # Добавляем фильтр по дате

@admin.register(BillingProduct)
class BillingProductAdmin(admin.ModelAdmin):
    list_display = ('billing', 'product', 'quantity', 'price', 'status')