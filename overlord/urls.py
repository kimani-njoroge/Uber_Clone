from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'signup/driver/',views.driver_signup,name = 'driver'),

]

