from django import forms
from Products.models import Product

# class Item_form(forms.Form):
#     name = forms.CharField(max_length=40)
#     price = forms.FloatField()
#     description = forms.CharField(max_length=200)
#     SKU = forms.CharField(max_length=30)
#     active = forms.BooleanField(required=False)


class Item_form (forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'