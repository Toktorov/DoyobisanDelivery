# Generated by Django 4.2.5 on 2023-09-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0006_alter_billing_billing_receipt_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='billing_receipt_type',
            field=models.CharField(default='Самовывоз', max_length=100, verbose_name='Вид получения товара'),
        ),
    ]
