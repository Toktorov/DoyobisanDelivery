# Generated by Django 4.2.5 on 2023-09-26 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='billingproduct',
            options={'verbose_name': 'Продукт биллинга', 'verbose_name_plural': 'Продукты биллингов'},
        ),
    ]
