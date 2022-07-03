
from distutils.command.upload import upload
from gettext import Catalog
from django.db import models

# Create your models here.


class Category(models.Model):
    name= models.CharField(max_length=30)
    created_at = models.DateField(blank=True,null=True)
    class Meta:
        verbose_name= "Category"
        verbose_name_plural ="Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    category=models.ForeignKey (Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    price = models.FloatField()
    created_at = models.DateField(blank=True,null=True)
    image=models.ImageField(upload_to='products',null=True, blank=True)
    SKU = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name= "Product"
        verbose_name_plural ="Products"

    def __str__ (self):
        return self.name
