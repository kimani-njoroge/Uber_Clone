from django.db import models

# Create your models here.
class Car(models.Model):
    car_brand = models.CharField(max_length=20)
    no_plate = models.CharField(max_length=25)
    no_seat = models.IntegerField(max_length=20)


class Driver(models.Model):
    driver_name = models.CharField(max_length=40)
    car = models.ForeignKey(Car)
    pickup_point = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)