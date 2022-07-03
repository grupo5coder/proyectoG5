
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from Products.models import Product
from Products.forms import Item_form

# Create your views here.
class List_products(ListView):
    model = Product
    template_name= 'products.html'
    queryset = Product.objects.filter(is_active = True)

class Create_item(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'create_item.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_item', kwargs={'pk':self.object.pk})


def search_item(request):
        articulos= Product.objects.filter(name__icontains = request.GET['search'])
        if articulos.exists():
            context = {'articulos':articulos}
        else:
            context = {'errors':'No se encontro el producto'}
        return render (request,'search_item.html', {'articulos':articulos,'query':request.GET['search'],'errors':f'Lo sentimos. El artículo buscado no existe en el catálogo'})

class Detail_item(DetailView):
    model = Product
    template_name= 'detail_item.html'

class Delete_item(DeleteView):
    model= Product
    template_name='delete_item.html'

    def get_success_url(self):
        return reverse('Product')


class Update_item(UpdateView):
    model = Product
    template_name= 'update_item.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detail_item', kwargs = {'pk':self.object.pk})



# def product (request):
#     items= Product.objects.all()
#     return render(request,'products.html',{'items':items})

# def create_item(request):
#     if request.method == 'GET':
#         form = Item_form()
#         return render(request, 'create_item.html', {'form':form})

#     elif request.method == 'POST':
#         form = Item_form(request.POST)
#         if form.is_valid():
#             new_item= Product.objects.create (
#                 name = form.cleaned_data['name'],
#                 description = form.cleaned_data['description'],
#                 price = form.cleaned_data['price'],
#                 created_at = form.cleaned_data['created_at'],
#                 SKU = form.cleaned_data['SKU'],
#                 image=form.cleaned_data['image'],
#                 is_active = form.cleaned_data['is_active'],)
#             context = {'new_item':new_item}
#         else:
#             context = {'errors':form.errors}
#         return render(request, 'create_item.html', context = context)

#     else:
#         return HttpResponse('Only GET and POST methods are allowed')

# def detail_item(request, pk):
#     try:
#         product = Product.objects.get(id=pk)
#         return render (request,'detail.item.html',{'product':product})
#     except:
#         return render (request, 'products.html',{'error':f'El producto no existe'})



