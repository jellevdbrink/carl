from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'name': 'CARL'
    }
    return render(request, 'recog_app/index.html', context)
