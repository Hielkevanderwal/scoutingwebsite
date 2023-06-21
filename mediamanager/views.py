from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
class UploadView(TemplateView):
    template_name = "upload.html"

class AlbumOverviewView(TemplateView):
    template_name = "media_index.html"

class AlbumView(TemplateView):
    template_name = "album.html"