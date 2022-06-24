from django.urls import path
from providers.views import list_providers, create_provider
urlpatterns = [
    path ("", list_providers, name = "list_providers"),
    path ("create_provider/", create_provider, name = "create_provider")
]