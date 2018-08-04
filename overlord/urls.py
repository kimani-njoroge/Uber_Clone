from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'signup/driver/',views.driver_signup, name = 'drive'),
    url(r'signup/rider/', views.rider_signup, name='ride'),

]

