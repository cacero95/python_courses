from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.list, name="list_article"),
    path('category/<int:category_id>', views.show_category, name="category"),
    path('article/<int:article_id>', views.get_article, name="article")
]