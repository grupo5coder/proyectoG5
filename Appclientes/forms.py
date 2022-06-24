
from django import forms



class Client_form(forms.Form):
    name = forms.CharField(max_length=40)
    fantacy_name = forms.CharField(max_length=40)
    namer_phone = forms.FloatField()
    date_create = forms.DateTimeField()
    adess = forms.CharField(max_length=200)
    city =  forms.CharField(max_length=200)
    Cuit = forms.CharField(max_length=30)
    active = forms.BooleanField()
