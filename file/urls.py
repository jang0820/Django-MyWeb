from . import views
from django.urls import path

app_name = "file"

urlpatterns = [
    path("", views.uploadFile, name = 'upload'),
    path('del/<int:pk>', views.deleteFile, name='delete'),
    path('download/<int:pk>', views.downloadFile, name='download'),
]