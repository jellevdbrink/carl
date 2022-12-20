from django.urls import path

from . import views

urlpatterns = [
    path('analyze', views.analyze, name='analyze'),
    path('<str:name>', views.result, name='result'),

    path('', views.index, name='index'),
]
