from django.db import models
from django.utils.timezone import now

# Create your models here.

class Provider(models.Model):
    name = models.CharField(max_length=40)
    contact = models.CharField(max_length=30)
    contact_number = models.IntegerField()
    next_purchase = models.DateField(default=now)

    class Meta:
        verbose_name= "Provider"
        verbose_name_plural ="Providers"

    def __str__ (self):
        return self.name