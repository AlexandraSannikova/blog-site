from django.urls import path, re_path
from loginsys import views

urlpatterns = [
    re_path('^login/', views.login),
    re_path('^logout/', views.logout),
    re_path('^register/', views.register)
]
