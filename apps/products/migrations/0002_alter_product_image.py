# Generated by Django 4.2.5 on 2023-10-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='no_image.jpg', max_length=1000, upload_to='', verbose_name='Фотография продукта'),
        ),
    ]
