from django.shortcuts import render

from apps.settings.models import Setting
from apps.products.models import Product

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    products = Product.objects.all()
    return render(request, 'index-8.html', locals())