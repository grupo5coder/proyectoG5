from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Contact_form(forms.Form):
    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()


class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Escriba nuevamente la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}
