"""ProyectoG5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ProyectoG5.views import index, contact, login_view, logout_view, register_view, about_us
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('contact/', contact , name= 'contact'),
    path('about_us/', about_us , name= 'about_us'),
    path('Products/', include('Products.urls')),
    path("list_providers/", include("providers.urls")),
    path("Client/", include ("Appclientes.urls")),

    path("login", login_view, name = "login"),
    path("logout/", logout_view, name = "logout"),
    path("register/", register_view, name = "register"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
