from overlord.models import User
from django.db import models

# Create your models here.


class Car(models.Model):
    car_brand = models.CharField(max_length=20)
    no_plate = models.CharField(max_length=25)
    no_seat = models.IntegerField(default=0)

    def __str__(self):
        return self.car_brand


class Driver(models.Model):
    driver_name = models.CharField(max_length=40)
    car = models.ForeignKey(Car)
    pickup_point = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    user = models.ForeignKey(User,blank=True)

    def passprofile_save(self):
        self.save()