from django.conf.urls import url
from . import views



urlpatterns=[
    url(r'^new/location/', views.passlock, name='newpass-lock'),
    url(r'^new/passprofile/', views.passprofile, name='newpass-profile'),


]
