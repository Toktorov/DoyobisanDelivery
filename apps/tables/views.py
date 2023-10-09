from django.shortcuts import render

from apps.settings.models import Setting
from apps.tables.models import Table, TableOrder, TableOrderItem
from apps.products.models import Product

# Create your views here.
def menu(request, table_uuid):
    table = Table(id=table_uuid)
    setting = Setting.objects.latest('id')
    products = Product.objects.all()
    return render(request, 'menu/index.html', locals())