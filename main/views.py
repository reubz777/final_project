from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {
    'title' : 'Главная',
    'content': 'Строительный магазин'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
    'title' : 'О нас',
    'content': 'О нас',
    'text_on_page': 'Сайт был написал как итоговый проект по курсам IT-academy'
    }
    return render(request, 'main/about.html', context)

def contact(request):
    context = {
    'title': 'Контактная информация',
    'content': 'Контактная информация',
    'text_on_page': 'gmail: reubz.student@gmail.com'
    }
    return render(request, 'main/contact.html', context)

def delivery(request):
    context = {
    'title': 'Доставка',
    'content': 'Доставка',
    'text_on_page': 'Тут должна быть информация об условии доставки'
    }
    return render(request, 'main/delivery.html', context)
