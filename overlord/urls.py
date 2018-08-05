from django.conf.urls import url
from . import views
# from django.contrib.auth import views


urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'accounts/signup/driver/',views.driver_signup, name = 'drive'),
    url(r'accounts/signup/rider/', views.rider_signup, name='ride'),
    url(r'accounts/driver/login/driverindex', views.driver_index, name='driver-index'),

]

