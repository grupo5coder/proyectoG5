from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from Appclientes.models import Client

# Hacer el formualario 
def client(request):
    print(request.method)
    client = Client.objects.all()
    context = {"Clientes":Client}
    return render(request, "clients.html",context=context)



