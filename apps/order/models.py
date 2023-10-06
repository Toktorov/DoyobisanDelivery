from django.db import models

from apps.tables.models import Table
from apps.products.models import Product

# Create your models here.
class Order(models.Model):
    session_key = models.CharField(max_length=40, unique=True, verbose_name="Ключ сессии")
    items = models.ManyToManyField(Product, through='OrderItem', verbose_name="Товары")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата формирования заказа")

    def __str__(self):
        return f"{self.session_key}"
    
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество товара")
    total = models.PositiveBigIntegerField(default=0, verbose_name="Итоговая цена товаров")

    def __str__(self):
        return f"{self.order}"
    
    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"