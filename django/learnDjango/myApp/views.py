from django.shortcuts import render, HttpResponse, redirect
from myApp.models import Article
from django.db.models import Q # is neccesary for make or sql queries with the django ORM
from myApp.forms import FormArticle
from django.contrib import messages # mensajes flash o mensajes de una sola sesion
# Create your views here.
menu = f"""
    <nav>
        <ul style="display:flex; justify-content:space-around;">
            <li>
                <a href="/">Index</a>
            </li>
            <li>
                <a href="/hi_world">Hi worlds</a>
            </li>
            <li>
                <a href="/contact/Andres">contact</a>
            </li>
        </ul>
    </nav>
"""

#def index(request):
#    out = "<ul>"
#    year = 1995
#    while year < 2020:
#        out += f"<li>{year}</li>"
#        year+=1
#    out += "</ul>"
#    return HttpResponse(
#    f"""
#        <h1>Inicio</h1>
#        </hr>
#        {menu}
#        </hr>
#        <p>Years from 1995 to 2020</p>
#        {out}
#    """
#    )

def index(request):
    """
    the first param is the request http
    the component to render
    the third is variables in this case is a dictionary
    """
    years = []
    year = 1995
    while year < 2020:
        years.append(year)
        year+=1
    return render(request, 'index.html', {
        'title_view': 'Index',
        'author': 'cacero95',
        'years': years,
        'my_variable': 'test data for the view'
    })

#def hi_world(request, number = 0):
#    if number == 1:
#        return redirect('/')
#    return HttpResponse(f"""
#        <h1>Hello world Django</h1>
#        <hr/>
#        {menu}
#    """)


def hi_world(request):
    return render(request, 'hi_world.html')

def contact(request, name="Andres"):
    return HttpResponse(menu+f"<h1>Contact {name}</h1>")
def filter_page(request):
    return render(request, 'filter_test.html' ,{
        'title':'Filter page',
        'array':[0,1,2,3,4,5]
    })

def create_article(request):
    # save a element in the dba with the models
    # article.save()
    return render(request, 'create_article.html')

def save_article(request, title, content, public):
    article = Article(
        title = title,
        content = content,
        public = public
    )
    article.save()
    messages.success(request, 'Article created')
    

def form_article(request):
    if request.method == 'POST':
        form = FormArticle(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data # get the data from the data
            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']
            save_article(request, title, content, public)
            return redirect('all_articles')
        else:
            return HttpResponse(
                "<span>Article could not saved</span>"
            )
    else:
        form = FormArticle() # Create a white form
    return render(request, 'form_article.html', {
        'form':form
    })
def article(request, title):
    try:
        # for select only one element from the dba use the get method 
        element = Article.objects.get(title=title, public=True)
        return HttpResponse(f"Article: {element.title} {element.content} ")
    except:
        return HttpResponse("Article was not found")
def update_article(request, id, title, public, content):
    try:
        element = Article.objects.get(id=id)
        element.title = title
        element.content = content
        element.public = public
        element.save()
        return HttpResponse(f"Article updated")
    except:
        return HttpResponse("Article was not found")
def getAll_articles(request):
    # for order the list use the order_by
    # when exist a - before the key the query order the list at reverse form
    # Article.objects.order_by('-title').all()
    # for limit the query is the next form
    # Article.objects[:3] the number is the quantity of element required
    # Article.objects.order_by('-title')[1:2] add an from and the limit to the query
    # [from:limit]
    # articles = Article.objects.all()
    # ------ ORM filters with django --------
    # with the method filter perform a query between the data according a condition
    # articles = Article.objects.filter(title='Batman')
    # for make gaps with the framework is the next form
    # articles = Article.objects.filter(title__contains="article")
    # in gaps also has a excact option key sensitive
    # articles = Article.objects.filter(title__iexact="article")
    # for make a query > or < is the next form
    articles = Article.objects.filter(id__gt=12)  # gt = >
    articles = Article.objects.filter(id__gte=12) # gt = >=
    articles = Article.objects.filter(id__lt=12)  # gt = <
    articles = Article.objects.filter(id__lte=12) # gt = <=
    articles = Article.objects.filter(id__lte=12, title__contains="deku") # is possible add more than one lookups
    articles = Article.objects.filter(
        id__gt=7
    ).exclude( # with the method exclude skip all the element below a condition
        public=False
    )
    # example of orm queries with a or condition
    articles = Article.objects.filter(
        Q(title__contains="deku") | Q(title__contains="batman")
    )
    # but in case that is neccesary make sql queries
    articles = Article.objects.raw("select * from myApp_article where title='Deku' and public=1")
    # order_by order the data below a condition
    articles = Article.objects.all().order_by('-id')
    return render(request, 'articles.html', {
        'articles': articles
    })

def delete_article(request, id=None, title=None):
    try:
        article = Article.objects.get(pk=id) if id else Article.objects.get(title=title)
        article.delete()
        return redirect('all_articles')
    except:
        return HttpResponse("The Article was not found")

def slider(request):
    return render(request, 'slider.html')