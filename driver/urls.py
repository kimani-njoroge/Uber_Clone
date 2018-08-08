from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^new/car/', views.carprofile, name='newdrive-car'),
    url(r'^new/driveprofile/', views.driveprofile, name='newdrive-profile'),
]
