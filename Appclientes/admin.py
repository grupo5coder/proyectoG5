from django.contrib import admin
from Appclientes.models import Clients

# Register your models here.

@admin.register(Clients)

class ClientsAdmin(admin.ModelAdmin):
    list_display=['name','city','Cuit']
    search_fields = ["name"]
    list_filter= ['name','Cuit']
