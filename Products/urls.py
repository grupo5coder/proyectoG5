from django.urls import path
from Products import views
from Products.views import product, create_item, search_item

urlpatterns =[
    path('', product, name = 'product'),
    path('create_item/', create_item, name = 'create_item'),
    path('search_item/', search_item, name = 'search_item'),
    # path('searching-pcts', searching_pcts),
    # path('contacto/', contacto, name = 'contacto'),
]
