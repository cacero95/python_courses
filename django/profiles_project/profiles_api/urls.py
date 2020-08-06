from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^hello_view/', views.HelloApiView.as_view()),
]