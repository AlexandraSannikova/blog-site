from django.shortcuts import render, redirect
#импортируем модели для выгрузки данных из БД
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from article.forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth # модуль в админке, для получения username
from datetime import datetime

def template_three_simple(request):
    view = "template_three"
    return render(request, 'myview.html', {'name': view}) # view и контекст

# отображение всех статей
def articles(request):
    #'articles.html' - разметка, 'articles' - что подставляем в разметку, берем это из БД
    return render(request, 'articles.html', {'articles': Article.objects.all(), 'username': auth.get_user(request).username})

# отображение одной статьи
def article(request, article_id=1):
    comment_form = CommentForm
    args = {} # словарь с переменными для шаблона
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)

    for i in args['comments']:
        print(i.comments_date)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render(request, 'article.html', args)

    # Добавление лайков
def addlike(request, article_id):
    try:
        article = Article.objects.get(id=article_id) # находим статью в модели
        article.article_likes+=1
        article.save() # сохранить в БД
    # если пользователь введет id, которого нет в БД, т е в БД не найдется и будет ошибка:
    except ObjectDoesNotExist:
        raise Http404 # Ошибка - не сущ-т запрошенная страница
    return redirect('/')

def addcomment(request, article_id):
    if(request.POST): # если данные в форме post-запроса
        form = CommentForm(request.POST) # экземпляр класса CommentForm с данными из запроса
        if form.is_valid(): # тут это особо не надо, тк просто текст
            # по умолч в ModelForm данные из браузера сразу сохр в БД, но у нас в форме нет comments_article
            #Но при этом comment становится равным комментарию(выше)
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            comment.comments_user = auth.get_user(request).username
            comment.comments_date = datetime.now()
            form.save()
    return redirect('/articles/get/%s/' % article_id) # возврат туда же, где написан коммент