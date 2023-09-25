from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True, null=True
    )
    price = models.CharField(
        max_length=100,
        verbose_name="Цена"
    )
    image = models.ImageField(
        max_length=1000,
        verbose_name="Фотография продукта"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"