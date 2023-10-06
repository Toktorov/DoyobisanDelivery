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
    
    def save(self, *args, **kwargs):
        if not self.number:
            self.number = str(uuid.uuid4().int)[:5]  # Генерируем UUID и оставляем только первые 20 цифр
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Стол"
        verbose_name_plural = "Столы"