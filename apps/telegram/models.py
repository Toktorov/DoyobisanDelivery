from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    username = models.CharField(
        max_length=200, verbose_name="Имя пользователя",
        blank=True, null=True
    )
    user_id = models.CharField(
        max_length=200,
        verbose_name="ID пользователя telegram"
    )
    first_name = models.CharField(
        max_length=200, verbose_name="Имя",
        blank=True, null=True
    )
    last_name = models.CharField(
        max_length=200, verbose_name="Фамилия",
        blank=True, null=True
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )

    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        verbose_name = "Телеграм пользователь"
        verbose_name_plural = "Телеграм пользователи"