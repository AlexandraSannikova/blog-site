from django.urls import path
from article import views

urlpatterns = [
    path('3/', views.template_three_simple)
]
