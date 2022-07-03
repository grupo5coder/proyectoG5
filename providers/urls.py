from django.urls import path
from providers.views import delete_provider, List_providers, Create_provider, Detail_provider, delete_provider, Edit_provider
urlpatterns = [
    path ("", List_providers.as_view(), name = "list_providers"),
    path ("create_provider/", Create_provider.as_view(), name = "create_provider"),
    path ("detail_provider/<int:pk>/", Detail_provider.as_view(), name = "detail_provider"),
    path ("delete_provider/<int:pk>/", delete_provider, name = "delete_provider"),
    path ("edit_provider/<int:pk>/", Edit_provider.as_view(), name = "edit_provider"),
]   