from django.db import models
from django.template.defaultfilters import slugify

from base.models import Speltak

class Photo(models.Model):
    photo = models.ImageField()

    def __str__(self):
        return self.photo.path
    
    def get_size(self):
        return self.photo.size

class Album(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)
    photo_count = models.IntegerField(default=0, editable=False)
    speltak = models.ManyToManyField(Speltak, blank=True)
    url_slug = models.SlugField(unique=True, blank=True)

    photos = models.ManyToManyField(Photo, related_name="album")
    thumbnail = models.ForeignKey(Photo, null=True, blank=True, on_delete=models.DO_NOTHING,related_name="thumbnail_of_album") 

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Album.objects.filter(url_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.url_slug:
            self.url_slug = self._get_unique_slug()
        
        super().save(*args, **kwargs)    

    def update_Album(self, *args, **kwargs):
        self.photo_count = self.photos.count()
        if self.photo_count > 0 and not self.thumbnail:
            self.thumbnail = self.photos.first()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name