from django.urls import path
from .views import AlbumView, AlbumOverviewView, AlbumUploadView, AlbumEditView

urlpatterns = [
    path("", AlbumOverviewView.as_view()),
    path("album/<slug:slug>/", AlbumView.as_view(), name="ablumview"),
    path("add", AlbumUploadView.as_view(), name="add album"),
    path("album/<slug:slug>/edit", AlbumEditView.as_view(), name="editview"),
]