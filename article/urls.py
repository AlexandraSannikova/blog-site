from django.urls import path, re_path
from article import views

urlpatterns = [
    # все
    re_path('^articles/all/$', views.articles),
    # одна статья. указываем, что будет передаваться параметр article_id и он должен быть цифрой
    re_path('^articles/get/(?P<article_id>\d+)/$', views.article),
    # для изменения лайков
    re_path('^articles/addlike/(?P<article_id>\d+)/$', views.addlike),
    re_path('^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment),
    # для отображения статей с базовым шаблоном main.html
    re_path('^', views.articles)
]
