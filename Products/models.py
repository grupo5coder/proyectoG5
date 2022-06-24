from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=400, blank=True, null=True)
    price = models.FloatField()
    created_at = models.DateField(blank=True,null=True)
    SKU = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name= "Product"
        verbose_name_plural ="Products"

    def __str__ (self):
        return self.name

