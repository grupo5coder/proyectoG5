
from multiprocessing.connection import Client
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from Appclientes.models import Clients
from Appclientes.forms import Client_form

# Hacer el formualario 
def client_view(request):
    print(request.method)
    clientes = Clients.objects.all()
    context = {"clientes":clientes}
    return render(request, "Client.html", context=context)

def new_client_view(request):

    if request.method == 'GET':
        form = Client_form()
        context = {"form":form}
        return render(request, 'Create_Client.html',context=context)
    else: 
        form = Client_form(request.POST)
        if form.is_valid ():
            new_client = Clients.objects.create(
                name =  form.cleaned_data['name'],
                fantacy_name = form.cleaned_data['fantacy_name'],
                namer_phone = form.cleaned_data['namer_phone'],
                date_create = form.cleaned_data['date_create'],
                adess = form.cleaned_data['adess'],
                city =  form.cleaned_data['city'],
                Cuit = form.cleaned_data['Cuit'],
                active = form.cleaned_data['active'],)
            context = {'new_client':new_client}
        else:
            context = {"error":form.errors}
        return render(request, 'Create_Client.html', context=context )

def search_client_view(request):
    clientebuscado = Clients.objects.filter(name__icontains = request.GET['searchclient'])
    if clientebuscado.exists():
        context = {'clientebuscado':clientebuscado}
    else:
        context = {'errors':'No se encontro el cliente'}

    return render (request,'Search_client.html', context = context)


def detall_client(request, pk):
    try:
        cliente = Clients.objects.get(id=pk)
        context = {"cliente":cliente}
        return render(request, "detall_client.html", context=context)
    except: 
        context = { "error" : "el producto no existe" }
        return render (request, "client.html", context=context)

