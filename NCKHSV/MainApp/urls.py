from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
]