from django.urls import path
from .views import UploadView, AlbumView, AlbumOverviewView

urlpatterns = [
    path("upload/<slug:slug>/", UploadView.as_view()),
    path("", AlbumOverviewView.as_view()),
    path("album/<slug:slug>/", AlbumView.as_view())
]