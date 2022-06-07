from multiprocessing.connection import Client
from django.contrib import admin

from django.urls import path

from ProyectoG5.views import index

from Appclientes.views import Client_view, new_client_view

urlpatterns = [


    path("",Client_view , name = "Client_view"),

    path("create-client/",new_client_view, name = "new_client_view"),

    
]