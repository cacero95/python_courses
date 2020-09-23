from django.shortcuts import render, HttpResponse, redirect
from record.forms import FormWord
from django.contrib import messages
from record.models import Word

# Create your views here.
def record(request):
    form = FormWord()
    return render(request, 'record.html', {
        'form': form
    })
def create_record(request):
    data = request.POST
    query = Word.objects.filter(content=data['content'])
    if len(query) == 0:
        word = Word(
            content = data['content'],
            content_type = data['content_type']
        )
        word.save()
        messages.success(request, 'Word saved')
        return redirect('record')
    else:
        return HttpResponse(
            f"""
                <h4>La palabra existe</h4>
            """
        )
