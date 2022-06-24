from django.contrib import admin
from Products.models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','description','price','is_active']
    search_fields = ["name"]
    list_filter= ['name','price']

