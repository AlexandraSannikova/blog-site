# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib import auth

def login(request):
    args = {} # словарь с переменными для шаблона
    args.update(csrf(request))
    if(request.POST): # если данные в форме post-запроса
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password) # авторизация - если есть такой - модель пользователя
        if user is not None:
            auth.login(request, user) # войти, создать сессию для пользователя
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render(request, 'login.html', args) # возвращаем форму логина
    else:
        return render(request, 'login.html', args) # возвращаем форму логина

def logout(request):
    auth.logout(request) # деавторизировать
    return redirect('/')