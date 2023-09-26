from django.db import models
from django.utils.translation import gettext as _
import uuid

from apps.products.models import Product

# Create your models here.
class Billing(models.Model):
    class BillingReceiptTypeChoices(models.TextChoices):
        PICKUP = 'Pickup', _('Самовывоз')
        DELIVERY = 'Delivery', _('Доставка')
    billing_receipt_type = models.CharField(
        max_length=100, choices=BillingReceiptTypeChoices.choices,
        default=BillingReceiptTypeChoices.DELIVERY,
        verbose_name=_('Вид получения товара')
    )
    total_price = models.PositiveIntegerField(
        verbose_name="Итоговая цена товаров"
    )
    payment_code = models.CharField(
        max_length=20, unique=True,
        verbose_name="Код оплаты биллинга",
    )
    status = models.BooleanField(
        default=False, verbose_name="Статус заказа"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания биллинга"
    )

    def __str__(self):
        return f"{self.billing_receipt_type} {self.payment_code}"
    
    def save(self, *args, **kwargs):
        if not self.payment_code:
            self.payment_code = str(uuid.uuid4().int)[:20]  # Генерируем UUID и оставляем только первые 20 цифр
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Биллинг"
        verbose_name_plural = "Биллинги"

class BillingProduct(models.Model):
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE, related_name='billing_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(verbose_name="Количество товаров")
    price = models.PositiveBigIntegerField(verbose_name="Цена товара")

    def __str__(self):
        return f"{self.billing} - {self.product} ({self.quantity} шт.)"
    
    class Meta:
        verbose_name = "Продукт биллинга"
        verbose_name_plural = "Продукты биллингов"