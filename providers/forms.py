from email.policy import default
from django import forms
# from django.utils.timezone import now

class Provider_form(forms.Form):
    name = forms.CharField(max_length=40)
    contact = forms.CharField(max_length=30)
    contact_number = forms.IntegerField()
    next_purchase = forms.DateField()