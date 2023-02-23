from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('manage/', views.manage, name='manage'),
    path('update/<int:id>/', views.update, name='update'),
    # path('detail/<int:id>/', views.house_detail, name='detail'),
]