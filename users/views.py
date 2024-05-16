from django.shortcuts import render


def login(request):
    context = {
        'title': 'Home - Авторизация',
    }
    return render(request, template_name='users/login.html', context=context)


def registration(request):
    context = {
        'title': 'Home - Регистрация',
    }
    return render(request, template_name='users/registration.html', context=context)


def profile(request):
    context = {
        'title': 'Home - Кабинет',
    }
    return render(request, template_name='users/profile.html', context=context)


def logout(request):
    pass
