from blog.models import Category, Article

def get_categories(request):
    # id__in is the lookup in which indicates all categories used in any public article at the dba
    ids = Article.objects.filter(public=True).values_list('categories', flat=True)
    return {
        'categories': Category.objects.filter(id__in=ids).values_list('id', 'name')
    }