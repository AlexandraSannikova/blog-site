from django.contrib import admin
from article.models import Article, Comments

class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    fields=['article_title','article_text', 'article_date']
    inlines = [ArticleInline]
    list_filter = ['article_date']

# Register your models here.
admin.site.register(Article, ArticleAdmin)