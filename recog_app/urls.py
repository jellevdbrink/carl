from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('analyze', views.result_by_analyze, name='result_by_analyze'),
    path('<str:product_name>', views.result_by_name, name='result_by_name'),

    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
