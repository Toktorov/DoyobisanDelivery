# Generated by Django 4.2.5 on 2023-10-21 02:46

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_receipt_type', models.CharField(default='Самовывоз', max_length=100, verbose_name='Вид получения товара')),
                ('total_price', models.PositiveIntegerField(verbose_name='Итоговая цена товаров')),
                ('address', models.CharField(max_length=300, verbose_name='Адрес доставки')),
                ('phone', models.CharField(max_length=200, verbose_name='Номер телефона')),
                ('payment_method', models.CharField(default='Наличные', max_length=100, verbose_name='Способ оплаты')),
                ('payment_code', models.CharField(max_length=20, unique=True, verbose_name='Код оплаты биллинга')),
                ('status', models.BooleanField(default=False, verbose_name='Статус заказа')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания биллинга')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='billing.billing')),
            ],
            options={
                'verbose_name': 'Биллинг',
                'verbose_name_plural': 'Биллинги',
            },
        ),
        migrations.CreateModel(
            name='BillingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество товаров')),
                ('price', models.PositiveBigIntegerField(default=0, verbose_name='Итоговая цена')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('billing', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billing_products', to='billing.billing')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Продукт биллинга',
                'verbose_name_plural': 'Продукты биллингов',
            },
        ),
        migrations.CreateModel(
            name='SaleSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Отчет продажа товар',
                'verbose_name_plural': 'Отчеты продажи товаров',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('billing.billing',),
        ),
    ]
