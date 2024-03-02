from django.shortcuts import render, redirect

from django.http import (
    HttpResponse, HttpResponseNotFound, Http404,
    HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Войти', 'url_name': 'login'},
    {'title': 'Добавить препарат', 'url_name': 'add_medicine'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
]

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def index1(r):
    return HttpResponse("index1")

def index(request):
    context = {
        'title': 'Главная страница',
        'content': 'Контент индекса',
        'menu': menu
 }
    return render(request, 'zdorov/index.html', context)


def about(request):
    context = {
        'title': 'О сайте',
        'content': 'Информация о сайте',
        'menu': menu,

    }
    return render(request, 'zdorov/about.html', context)

def contact(request):
    return HttpResponse('Обратная связь')

def add_medicine(request):
    return HttpResponse('Добавить препарат')

def login(request):
    return HttpResponse('Войти')

def categories(request, cat_id):
    context = {
        'title': f'Категория {cat_id}',
        'content': f'Контент категории  {cat_id}'

    }
    return render(request, 'zdorov/index.html', context)


def categories_by_slug(request, cat_slug):
    print(request.GET)
    context = {
        'title': f'Категория {cat_slug}',
        'content': f'Контент категории по слагу {cat_slug}'

    }
    return render(request, 'zdorov/index.html', context)



def archive(request, year):
    year = int(year)
    if year > 2050:
        uri = reverse('cats', args=('music',))
        return redirect(uri)
    if year < 1910:
        return redirect(index, permanent=True)
    # if year > 3000:
    #     raise Http404()
    context = {
        'title': f'Год {year}',
        'content': f'Год {year}'

    }
    return render(request, 'zdorov/index.html', context)
