
from django import forms
from Appclientes.models import Clients 



#class Client_form(forms.Form):
#    name = forms.CharField(max_length=40)
#    fantacy_name = forms.CharField(max_length=40)
#    namer_phone = forms.FloatField()
#    
#    adess = forms.CharField(max_length=200)
#    city =  forms.CharField(max_length=200)
#    Cuit = forms.CharField(max_length=30)
#    active = forms.BooleanField()

class Client_form(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'