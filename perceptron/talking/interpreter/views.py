from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from record.models import Word
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def rules( word, negation, status_comment ):
    word = word.lower()
    type_comment = False
    if word == 'no':
        negation = True
    elif not word == 'pero' and not word == 'embargo' and not word == 'aunque':
        query = Word.objects.get(content=word)
        if query:
            type_comment = query.content_type
            if negation == True:
                type_comment = not type_comment
                negation = not negation
            status_comment = status_comment - 1 if type_comment == False else status_comment + 1  

    return {
        "negation": negation,
        "status_comment": status_comment
    }


@csrf_exempt
def interpreter(request):
    if request.method == 'POST':
        data = request.POST['phrase']
        comment_features = {
            "negation": False,
            "status_comment": 0
        }
        data = data.split()
        for word in data:
            comment_features = rules(
                    word,
                    comment_features['negation'], 
                    comment_features['status_comment'],
                )
        out = 'neutral'
        if comment_features['status_comment'] > 0:
            out = 'positive'
        elif comment_features['status_comment'] < 0:
            out = 'negative'
        return JsonResponse({
            'status': 200,
            'message': request.POST['phrase'],
            'out': out
        })
    return JsonResponse({
        'status': '400',
        'messsage': 'BAD_REQUEST'
    })