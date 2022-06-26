
from django.urls import path
from Appclientes.views import client_view, search_client_view , new_client_view , detall_client , delete_client

urlpatterns = [
    path("",client_view, name = "Client"),
    path("create-client/",new_client_view, name = "new_client_view"),
    path('search-client/', search_client_view, name = 'search_client_view' ),
    path("detall-client/<int:pk>/", detall_client , name = "detall_client" ), 
    path("delete-client/<int:pk>/", delete_client , name = "delete_client" ),
 

    ]



