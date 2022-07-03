from django.contrib import admin
from Products.models import Product, Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','created_at']
    search_fields = ['name']
    list_filter= ['name','created_at']




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','description','price','is_active']
    search_fields = ["name"]
    list_filter= ['name','price']

