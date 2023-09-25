from django.db import models

from apps.products.models import Product

# Create your models here.
class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True, verbose_name="Ключ сессии")
    items = models.ManyToManyField(Product, through='CartItem', verbose_name="Товары")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания корзины")

    def __str__(self):
        return f"{self.session_key}"
    
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Корзина")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество товара")

    def __str__(self):
        return f"{self.cart}"
    
    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"