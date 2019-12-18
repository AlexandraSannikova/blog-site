# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

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

def register(request):
    args = {} # словарь с переменными для шаблона
    args.update(csrf(request))
    args['form'] = UserCreationForm() #создаем пустую форму
    if(request.POST): # отправлены ли данные из адресной строки или формы регистрации пользователя
        newuser_form = UserCreationForm(request.POST) # тоже новая форма, но с данными из запроса (с username, password1 и 2)
        if newuser_form.is_valid():
            newuser_form.save() # т к встроенная форма наследуется от ModellForm, достаточно вызвать save(), чтобы сохр сразу в БД
            # данные username и password из формы, получаем юзера и логинимся
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser) # войти, создать сессию для пользователя
            return redirect('/')
        else:
            args['form'] = newuser_form # т к после проверки на валидноть, могут находиться ошибки в форме, добавленные автоматич
    return render(request, 'register.html', args) # возвращаем форму, когда у нас нет запроса
