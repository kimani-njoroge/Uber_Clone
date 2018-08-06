from django import forms
from .models import Driver, Car

class DriverProfileForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = ['user']


class CarProfile(forms.ModelForm):
    class Meta:
        model = Car
