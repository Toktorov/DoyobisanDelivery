# Generated by Django 4.2.5 on 2023-10-21 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_alter_table_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'verbose_name': 'Стол', 'verbose_name_plural': 'Столы'},
        ),
    ]
