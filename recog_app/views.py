from django.shortcuts import render, redirect

from recog_app.forms import IngredientForm
from recog_app.models import Product

recognized = ['apple', 'tomato', 'pear']

def index(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            return redirect('result', form.cleaned_data['name'])

    context = {
        'form': IngredientForm()
    }
    return render(request, 'recog_app/index.html', context)

def result(request, name=''):
    # Find/Create a Product instance based on the ingredient name
    product = Product(name, 'test url', ['test recipe'], ['test video'])

    context = {
        'product': product
    }
    return render(request, 'recog_app/result.html', context)

def analyze(request):
    # Analyze the image and redirect to result page with the found ingredient name
    name = 'apple'

    return redirect('result', name)
