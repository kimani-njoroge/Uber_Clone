from django import forms
from .models import Passenger, Location


class PassProfileForm(forms.ModelForm):
    class Meta:
        model = Passenger
        exclude = ['user']

class PassLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ['longitude','latitude']

