from django.shortcuts import render

# Create your views here.

def catalog(request):
    context = {
    'title': 'Каталог',
    'goods': [
        {'image': '',
         'name': 'Отвёртка',
         'description': 'Красная отвертка с кретообразным наконечником',
         'price': 15.00},

         {'image': '',
         'name': 'Напильник',
         'description': 'Напильник А-класса',
         'price': 3.00},

        ]
    }
    return render(request,'goods/catalog.html', context)

def product(request):
    return render(request,'goods/product.html')