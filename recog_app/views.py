from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from recog_app.forms import ImageForm, IngredientForm
from recog_app.models import products

def index(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            return redirect('result', form.cleaned_data['name'])

    context = {
        'ingredient_form': IngredientForm(),
        'image_form': ImageForm()
    }
    return render(request, 'recog_app/index.html', context)

def result(request, product):
    # Find a Product instance based on the ingredient name
    if type(product) == str:
        for prod in products:
            if prod.name == product:
                product = prod
                break

    if type(product) == str:
        return HTTPResponse('We cannot find the product')
    
    if product.certainty > 0.7:
        context = {
            'ingredient_form': IngredientForm(),
            'product': prod
        }
        return render(request, 'recog_app/result.html', context)

    # Hardcoded array of products
    context = {
        'products': products
    }
    return render(request, 'recog_app/unknown.html', context)

def analyze(request):
    # Analyze the image and redirect to result page with the found ingredient name
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fss = FileSystemStorage()
            file = fss.save(image.name, image)
            file_url = fss.url(file)
            # Met de file_url kan je nu alles doen met de picca wat je maar wil
            
            print(file_url)
            
            name = 'apple'
            
            return redirect('result', name)

    return redirect('index')
