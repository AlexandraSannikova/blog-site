from django.db import models

class Article(models.Model):
    class Meta():
        db_table = "article"
    
    article_title = models.CharField(max_length = 200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)

class Comments(models.Model):
    class Meta():
        db_table = "comments"
        
    #текст коммента
    comments_text = models.TextField()
    
    #создать отношение с Article
    comments_artice = models.ForeignKey(Article, on_delete=models.PROTECT)
    