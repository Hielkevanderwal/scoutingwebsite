from django.urls import path
from .views import UploadView, AlbumView, AlbumOverviewView

urlpatterns = [
    path("upload/", UploadView.as_view()),
    path("", AlbumOverviewView.as_view()),
    path("Album/", AlbumView.as_view())
]