from django.contrib import admin
from providers.models import Provider

# Register your models here.

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display=['name','contact','contact_number']
    search_fields = ["name"]
    list_filter= ['name','next_purchase']