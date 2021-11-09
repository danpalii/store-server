from django.shortcuts import render
import datetime

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
    }
    return render(request, 'products/products.html', context)

def test_context(request):
    context = {
        'title': 'store',
        'header': 'Hello!',
        'username': 'Ivan Ivan',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
        ],
        #'promotion': True,
        'products_of_promotion':[
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00, 'date': datetime.datetime(year=2021, month=11, day=9)},
        ]
    }
    return render(request, 'products/test-context.html', context)
