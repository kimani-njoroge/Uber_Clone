from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=40)
    longitude = models.IntegerField(default=0)
    latitude = models.IntegerField(default=0)
