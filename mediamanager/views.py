from django.shortcuts import render, get_object_or_404

from django.views.generic import TemplateView

from .models import Album

# Create your views here.
class UploadView(TemplateView):
    template_name = "upload.html"

class AlbumOverviewView(TemplateView):
    
    def get(self, request):
        context = {
            "Albums": Album.objects.all()
        }
        print(context)

        return render(request, "album_overview.html", context)


class AlbumView(TemplateView):

    def get(self, request, slug):
        print(slug)

        context = {
            "Album": get_object_or_404(Album, url_slug=slug)
        }

        return render(request, "album.html", context)