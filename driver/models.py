from django.db import models

# Create your models here.
class Car(models.Model):
    car_brand = models.CharField(max_length=20)
    no_plate = models.CharField(max_length=25)
    no_seat = models.IntegerField(max_length=20)


