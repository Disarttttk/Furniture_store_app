from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': True
    }
    return render(request, template_name='main/index.html', context=context)


def about(request):
    return HttpResponse('About page')
