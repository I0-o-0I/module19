from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegister
from .models import *
from random import randint
from django.core.paginator import Paginator



def platform(request):
    return render(request, 'platform.html')

def games(request):
    context = {
        'game': Game.objects.all(),
    }
    return render(request, 'games.html', context)

def cart(request):
    return render(request, 'cart.html')

# def sign_up_by_html(request):
#     info = {}
#     context = {
#         'info': info
#     }
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repeat_password = request.POST.get('repeat_password')
#         age = request.POST.get('age')
#
#         if password != repeat_password:
#             info['error'] = 'Пароли не совпадают'
#             return HttpResponse('Пароли не совпадают')
#         elif int(age) < 18:
#             info['error'] = 'Вы должны быть старше 18'
#             return HttpResponse('Вы должны быть старше 18')
#         elif username in list_user:
#             info['error'] = 'Пользователь уже существует'
#             return HttpResponse('Пользователь уже существует')
#         else:
#             list_user.append(username)
#             return HttpResponse(f'Приветствуем, {username}!')
#
#     return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_django(request):
    info = {}
    context = {
        'info': info
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return HttpResponse('Пароли не совпадают')
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return HttpResponse('Вы должны быть старше 18')
            elif Buyer.objects.filter(name=username):
                info['error'] = 'Пользователь уже существует'
                return HttpResponse('Пользователь уже существует')
            else:
                Buyer.objects.create(name=username, age=age, balance=randint(0,1000))
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', context)

def Newss(request):
    post = News.objects.all().order_by('-date')
    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    news_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'news': news_obj})

