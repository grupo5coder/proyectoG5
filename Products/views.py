
from django.shortcuts import render
from django.http import HttpResponse

from Products.models import Product
from Products.forms import Item_form

# Create your views here.

def product (request):
    items= Product.objects.all()
    return render(request,'products.html',{'items':items})


def create_item(request):
    if request.method == 'GET':
        form = Item_form()
        return render(request, 'create_item.html', {'form':form})

    elif request.method == 'POST':
        form = Item_form(request.POST)
        if form.is_valid():
            new_item= Product.objects.create (
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                price = form.cleaned_data['price'],
                created_at = form.cleaned_data['created_at'],
                SKU = form.cleaned_data['SKU'],
                is_active = form.cleaned_data['is_active'],)
            context = {'new_item':new_item}
        else:
            context = {'errors':form.errors}
        return render(request, 'create_item.html', context = context)

    else:
        return HttpResponse('Only GET and POST methods are allowed')


def search_item(request):
    articulos= Product.objects.filter(name__icontains = request.GET['search'])
    if articulos.exists():
        context = {'articulos':articulos}
    else:
        context = {'errors':'No se encontro el producto'}
    return render (request,'search_item.html', context = context)




