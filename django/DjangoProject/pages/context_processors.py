from pages.models import Page

def get_pages(request):
    # the flat=True convert the data to a list
    return {
        'pages': Page.objects.filter(visible=True).values_list('id', 'title', 'slug')
    }