"""learnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myApp.views

# in case when the path change if the name is the same the redirect will find the path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myApp.views.index, name="index"),
    path('hi_world/', myApp.views.hi_world, name="hi_world"),
    path('hi_world/<int:number>', myApp.views.hi_world, name="hi_world"),
    path('contact/', myApp.views.contact, name="contact"),
    path('contact/<str:name>', myApp.views.contact, name="contact"),
    path('filter/', myApp.views.filter_page, name="filter"),
    path('create_article/', myApp.views.create_article, name="create_article"),
    path('form_article/', myApp.views.form_article, name="form_article"),
    path('save_article/', myApp.views.save_article, name="save_article"),
    path('article/<str:title>', myApp.views.article, name="article"),
    path('update_article/<str:id>/<str:title>/<str:content>/<str:public>', myApp.views.update_article, name="update_article"),
    path('all_articles', myApp.views.getAll_articles, name="all_articles"),
    path('delete_articles/<int:id>', myApp.views.delete_article, name="delete_articles"),
    path('delete_articles/<str:title>', myApp.views.delete_article, name="delete_articles"),
    path('slider/', myApp.views.slider, name="slider")
]
