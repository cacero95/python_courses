from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article

# Create your views here.
def list(request):
    articles = Article.objects.all()
    for art in articles:
        categories = art.categories.all()
        for cat in categories:
            print(cat.description)
    return render(request, 'articles/list.html', {
        'title': 'Articles',
        'articles': articles
    })

def show_category(request, category_id):
    # get_object_or_404 funtion will make the request
    # if the object exist the page display the info
    # otherwise display the 404 page
    category  = get_object_or_404(Category, id=category_id)
    """
    like the models category and articles are related exist a direct relationship
    and inverse relation, for that reason category.article_set.all contains
    all the articles related with the category and the next
    query is not neccesary
    """
    # articles = Article.objects.filter(categories=category_id)
    return render(request, 'categories/category.html', {
        'category': category
    })

def get_article(request, article_id):
    return render(request, 'articles/article.html', {
        'article': get_object_or_404(Article, id=article_id)
    })