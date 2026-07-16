from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contact, view_product, create_category, create_product, matplot

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('view_product/<int:pk>', view_product, name='view_product'),
    path('create_category/', create_category, name='create_category'),
    path('create_product/', create_product, name='create_product'),
    path('matplot/', matplot, name='matplot'),
]