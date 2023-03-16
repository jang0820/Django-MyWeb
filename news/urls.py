from django.urls import path
from .views import NewsListView, NewsCreateView, NewsUpdateView, NewsDeleteView, NewsDetailView, downloadFile

app_name = 'news'
urlpatterns = [
    path('', NewsListView.as_view(), name='list'),
    path('create', NewsCreateView.as_view(), name='create'),
    path('update/<int:pk>', NewsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', NewsDetailView.as_view(), name='detail'),
    path('download/<int:pk>/<int:num>', downloadFile, name='download'),
]
