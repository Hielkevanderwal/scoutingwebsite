from django.db import models
from django.template.defaultfilters import slugify


# todo move to organisation app
class Speltak(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField()
    foto_count = models.IntegerField(default=0, editable=False)

    speltak = models.ManyToManyField(Speltak, blank=True)

    url_slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.url_slug:
            self.url_slug = slugify((self.name, self.speltak.all()))
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    photo = models.ImageField()
    description = models.TextField(blank=True, null=True)