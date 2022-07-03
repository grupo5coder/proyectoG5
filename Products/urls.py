from django.urls import path
from Products import views
from Products.views import List_products, Create_item, search_item, Detail_item, Delete_item, Update_item
# from Products.views import product, create_item, search_item

urlpatterns =[
    path('', List_products.as_view(), name = 'Product'),
    path('create_item/', Create_item.as_view(), name = 'create_item'),
    path('search_item/', search_item, name = 'search_item'),
    path('detail_item/<int:pk>/', Detail_item.as_view(), name = 'detail_item'),
    path('delete_item/<int:pk>/', Delete_item.as_view(), name = 'delete_item'),
    path('update_item/<int:pk>/', Update_item.as_view(), name = 'update_item')
]

