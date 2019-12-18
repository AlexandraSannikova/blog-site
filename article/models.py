# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

class Article(models.Model):
    class Meta():
        db_table = "article"
        ordering = ["-article_date"]

    article_title = models.CharField(max_length = 200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)

class Comments(models.Model):
    class Meta():
        db_table = "comments"

    comments_date = models.DateTimeField(default=datetime.now())
    #текст коммента
    comments_text = models.TextField(verbose_name="Текст комментария")
    
    #создать отношение с Article
    comments_article = models.ForeignKey(Article, on_delete=models.PROTECT)

    comments_user = models.TextField()

    