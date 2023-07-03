from django.contrib import admin
from .models import Album, Speltak, Photo

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'upload_date', 'photo_count')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'album', "get_size")
# Register your models here.
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)