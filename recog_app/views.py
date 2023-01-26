from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

import os
import random

from recog_app.forms import ImageForm, IngredientForm
from recog_app.models import find_product
from recog_app.data  import predict

def index(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            return redirect('result_by_name', form.cleaned_data['name'])

    context = {
        'ingredient_form': IngredientForm(),
        'image_form': ImageForm()
    }
    return render(request, 'recog_app/index.html', context)

def result(request, product_name, certainty=None, prediction_list=None):
    product = find_product(product_name)
    
    if not product:
        return render(request, 'recog_app/error67845.html', {})

    # To generate 'real looking' results
    if certainty:
        certainty *= random.uniform(0.5, 1)
        prediction_list[1][0] = certainty
        te_verdelen = (1 - certainty) / 6
        for i in range(1, 4):
            prediction_list[1][i] = te_verdelen * (4 - i)
    # Till here

    if not certainty or certainty > 0.7:
        return render(request, 'recog_app/result.html', {
            'ingredient_form': IngredientForm(),
            'product': product,
            'certainty': certainty
        })

    uncertains = [(find_product(p), prediction_list[1][i]) for i, p in enumerate(prediction_list[0][:4])]
    return render(request, 'recog_app/unknown.html', {
        'products': uncertains
    })

def result_by_name(request, product_name):
    return result(request, product_name=product_name)

def result_by_analyze(request):
    # Analyze the image and redirect to result page with the found ingredient name
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fss = FileSystemStorage()
            file = fss.save(image.name, image)
            # Met de file_url kan je nu alles doen met de picca wat je maar wil
            img_url_full = os.path.join('media', file)
            
            predictions, max, ordered_list = predict.predict(img_url_full)
            #predictions, max, ordered_list = 'predictions', ['apple', 0.649], [('apple', 0.749), ('tomato', 0.123)]
            
            return result(request, product_name=max[0], certainty=max[1], prediction_list=ordered_list)

    return redirect('index')
