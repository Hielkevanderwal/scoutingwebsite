from django.db import models

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
    foto_count = models.IntegerField(default=0)

    speltak = models.ManyToManyField(Speltak, blank=True)

    def __str__(self):
        return self.name