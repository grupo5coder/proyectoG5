from django.db import models

# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=40)
    fantacy_name = models.CharField(max_length=40)
    namer_phone = models.FloatField()
    date_create = models.DateTimeField()
    adess = models.CharField(max_length=200)
    city =  models.CharField(max_length=200)
    Cuit = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__ (self):
        return self.name