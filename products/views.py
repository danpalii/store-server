from django.shortcuts import render

from products.models import Product, ProductCategory

# Create your views here.
# Controalele = views = functii

def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Katalog',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)

