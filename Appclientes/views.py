
from http import client
from multiprocessing import context

from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from Appclientes.models import Clients
from Appclientes.forms import Client_form
from django.views.generic import ListView , DeleteView , DetailView, UpdateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Hacer el formualario 
def client_view(request):
    print(request.method)
    clientes = Clients.objects.all()
    context = {"clientes":clientes}
    return render(request, "Client.html", context=context)
    
#   class List_client(ListView):     # Nombre por defecto = Objet_list
#       model: Clients
#       template_name: "Client.html"
#       queryset = Products.objects.filtrer(is_active=True)    #  Me filtra los objetos. 

def new_client_view(request):
    if request.user.is_authenticated:
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
                    
                    adess = form.cleaned_data['adess'],
                    city =  form.cleaned_data['city'],
                    Cuit = form.cleaned_data['Cuit'],
                    active = form.cleaned_data['active'],)
                context = {'new_client':new_client}
            else:
                context = {"error":form.errors}
            return render(request, 'Create_Client.html', context=context )
    else:
            return redirect('login')

def search_client_view(request):
    clientebuscado = Clients.objects.filter(name__icontains = request.GET['searchclient'])
    if clientebuscado.exists():
        context = {'clientebuscado':clientebuscado}
    else:
        context = {'errors':'No se encontro el cliente'}

    return render (request,'Search_client.html', context = context)

def detall_client(request, pk):
    try :
        cliente = Clients.objects.get(id=pk)
        context = {"cliente":cliente}
        return render(request, "detall_client.html", context=context)
    except: 
        context = { "error" : "el cliente no existe" }
        return render (request, "client.html", context=context)

def delete_client(request, pk):
    if request.user.is_authenticated:
        if request.method == "GET":

            cliente = Clients.objects.get(id=pk)
            context = {"cliente":cliente}

        else: 
            cliente = Clients.objects.get(id=pk)
            cliente.delete()
            context = {"message":"El cliente fue elimiando Correcto"} 

        return render(request,"delete_Client.html",context=context)
    else:
            return redirect('login')

   
class update_client(LoginRequiredMixin,UpdateView):
    model = Clients
    template_name = "update_client.html"
    
    fields = "__all__"

    def get_success_url(self) :
        return reverse("detall_client",kwargs={"pk":self.object.pk})


