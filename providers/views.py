from django.urls import reverse
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from providers.models import Provider
from providers.forms import Provider_form
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

 # def list_providers(request):
 #     list_providers = Provider.objects.all()
 #     context = {"list_providers":list_providers}
#     return render(request, "list_providers.html", context = context)

class List_providers(ListView):
    model = Provider
    template_name= 'list_providers.html'


class Create_provider(LoginRequiredMixin,CreateView):
    model = Provider
    template_name = 'create_provider.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse ('detail_provider', kwargs= {"pk":self.object.pk})

# def create_provider(request):
#     if request.user.is_authenticated:
#         if request.method == "GET":
#                 form = Provider_form()
#                 context = {"form":form}
#                 return render (request, "create_provider.html", context = context)
#         else:
#             form = Provider_form(request.POST)
#             if form.is_valid():
#                 new_provider = Provider.objects.create(
#                 name = form.cleaned_data["name"],
#                 contact = form.cleaned_data["contact"],
#                 contact_number = form.cleaned_data["contact_number"],
#                 next_purchase = form.cleaned_data["next_purchase"], 
#                 )
#                 context={"new_provider":new_provider}
#             return render (request, "create_provider.html", context=context)
#     else:
#         return redirect('login')



# def detail_provider(request, pk):
#     try: 
#         provider = Provider.objects.get(pk=pk)
#         context = {"provider":provider}
#         return render (request, "detail_provider.html", context=context)
#     except:
#         context = {"Error, no se puede eliminar el proveedor"}
#         return render(request, "list_providers.html", context=context)

class Detail_provider(DetailView):
    model = Provider
    template_name= 'detail_provider.html'

        

def delete_provider(request, pk):
    if request.user.is_authenticated:    
        try:
            if request.method == "GET":
                provider = Provider.objects.get(id=pk)
                context = {"provider":provider}
            else:
                provider = Provider.objects.get(pk=pk)
                provider.delete()
                context = {"message": "Proveedor eliminado correctamente"}
            
            return render(request, "delete_provider.html", context=context )

        except:
                context  = {"Error, no se pudo eliminar el proveedor"}
                return render(request, "delete_provider.html", context=context)
    else:
        return redirect('login')

class Edit_provider(LoginRequiredMixin, UpdateView):
    model = Provider
    template_name = "edit_provider.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("detail_provider", kwargs = {'pk':self.object.pk})
