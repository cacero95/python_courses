from django.shortcuts import render, HttpResponse, redirect

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
    return render(request, 'index.html')

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
    print(request)
    return HttpResponse(menu+f"<h1>Contact {name}</h1>")