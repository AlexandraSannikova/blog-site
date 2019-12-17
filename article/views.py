from django.shortcuts import render
#импортируем модели для выгрузки данных из БД
from article.models import Article, Comments

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
