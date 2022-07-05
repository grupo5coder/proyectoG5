
from urllib import request
from django import views
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect, render
from django.template import Template, context
from django.template.loader import get_template
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from ProyectoG5.forms import Contact_form, User_registration_form
from users.models import User_profile 

def index (request):
    print(request.user)
    print(request.user.is_authenticated)
    return render(request,'index.html')

def about_us (request):
    return render(request,'about_us.html')

def contact (request):
    if request.method=="POST":
        my_form= Contact_form(request.POST)
        if my_form.is_valid():
            inf=my_form.cleaned_data
            return render (request, 'gracias.html', {'inf':inf})
    else:
        my_form=Contact_form()
    return render (request, 'contact.html',{'my_form':my_form})

def login_view(request):
     
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context = {"message":f"Bienvenido {username}!"} 
                return render(request, "index.html", context=context)
            else:
                context = {"error":"No existe el usuario"}
                form = AuthenticationForm()
                return render(request, "auth/login.html", context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {"errors": errors, "form": form}
            return render(request, "auth/login.html", context = context)

    else:
        form = AuthenticationForm()
        context ={"form":form}
        return render(request, "auth/login.html", context = context)

def logout_view(request):

    logout(request)
    return redirect("index")

def register_view(request):
    if request.method == "POST":
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {"message": "Usuario creado con éxito!"}
            return render (request, "index.html", context = context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {"errors":errors, "form":form}
            return render(request, "auth/register.html", context=context)

    else:
        form = User_registration_form
        context = {"form": form}
        return render (request, "auth/register.html", context = context)
