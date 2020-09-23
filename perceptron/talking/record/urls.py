from django.urls import path
from . import views

urlpatterns = [
    path('record/', views.record, name='record'),
    path('create_record', views.create_record, name="create_record")
]