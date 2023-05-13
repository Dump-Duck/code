from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('search/', views.search, name='search_result'),
    path('filter/', views.filter, name='filter_result'),
    path('index/<int:id>', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('manage/', views.manage, name='manage'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('map/', views.map, name='map'),
    path('info/<int:id>', views.info_content, name='info'),
]