from multiprocessing.connection import Client
from django.contrib import admin

from django.urls import path

from ProyectoG5.views import index

from Appclientes.views import client_view, new_client_view

urlpatterns = [


    path("",client_view , name = "client_view"),

    path("create-client/",new_client_view, name = "new_client_view"),

    
]