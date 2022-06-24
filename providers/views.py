from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from providers.models import Provider
from providers.forms import Provider_form

# Create your views here.

def list_providers(request):
    list_providers = Provider.objects.all()
    context = {"list_providers":list_providers}
    return render(request, "list_providers.html", context = context)

def create_provider(request):
    if request.method == "GET":
        form = Provider_form()
        context = {"form":form}
        return render (request, "create_provider.html", context = context)
    else:
        form = Provider_form(request.POST)
        if form.is_valid():
            new_provider = Provider.objects.create(
                name = form.cleaned_data["name"],
                contact = form.cleaned_data["contact"],
                contact_number = form.cleaned_data["contact_number"],
                next_purchase = form.cleaned_data["next_purchase"], 
            )
            context={"new_provider":new_provider}
        return render (request, "create_provider.html", context=context)