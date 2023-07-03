from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import TemplateView

from .models import Album, Speltak, Photo

# Create your views here.
class AlbumEditView(TemplateView):
    
    def get(self, request, slug):
        context = {
            "Album": Album.objects.get(url_slug=slug),
            "speltakken": Speltak.objects.all()
        }
        return render(request, "album_edit.html", context)

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
    
class AlbumUploadView(TemplateView):
    def get(self, request):

        context = {"speltakken": Speltak.objects.all()}

        return render(request, "album_edit.html", context)
    
    def post(self, request, slug=None, **kwargs):
        data = request.POST
        images = request.FILES.getlist("images")
        print(images)

        new_album = Album.objects.create(
            name = data["Album name"],
            description = data["description"],  
        )
        new_album.speltak.add(Speltak.objects.get(name=data["speltak"]))
        
        for image in images:
            new_photo = Photo.objects.create(
                photo = image
            )
            new_album.photos.add(new_photo)

        new_album.update_Album()

        return redirect("ablumview", new_album.url_slug)