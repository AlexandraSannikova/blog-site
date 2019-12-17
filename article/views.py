from django.shortcuts import render, redirect
#импортируем модели для выгрузки данных из БД
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404

def template_three_simple(request):
    view = "template_three"
    return render(request, 'myview.html', {'name': view}) # view и контекст

# отображение всех статей
def articles(request):
    #'articles.html' - разметка, 'articles' - что подставляем в разметку, берем это из БД
    return render(request, 'articles.html', {'articles': Article.objects.all()})

# отображение одной статьи
def article(request, article_id=1):
    # получение конкретной статьи и комментариев для нее
    return render(request, 'article.html', {'article': Article.objects.get(id=article_id),'comments': Comments.objects.filter(comments_article_id=article_id)})

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