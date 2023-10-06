from django.db import models
import uuid

# Create your models here.
class Table(models.Model):
    number = models.IntegerField(
        verbose_name="Номер стола",
        unique=True
    )
    created = models.DateTimeField(
        verbose_name="Дата добавления",
        auto_now_add=True
    )

    def __str__(self):
        return str(self.number)
    
    class Meta:
        verbose_name = "Стол"
        verbose_name_plural = "Столы"