from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index_2'),
    path('about/', views.about, name='about'),
]