from django.forms import ModelForm
from article.models import Comments

#будет выводить на экран все поля, которые описаны в модели Comments
class CommentForm(ModelForm):
    class Meta:
        # форма модели привязана к модели, наша - к модели Comments
        model = Comments
        fields = ['comments_text'] # чтобы не вставлять comments_article (иначе юзер сможет выбрать статью)