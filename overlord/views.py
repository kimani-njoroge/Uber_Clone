from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import DriverSignupForm, RiderSignupForm
from driver.models import Driver

User = get_user_model()
# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')


def driver_signup(request):
    if request.method == 'POST':
        form = DriverSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_passenger = False
            user.is_driver = True
            user.save()
            return redirect('/')
    else:
        form = DriverSignupForm()
    return render(request,'registration/driver_signup.html',{'form':form})


def rider_signup(request):
   if request.method == 'POST':
       form = RiderSignupForm(request.POST)
       if form.is_valid():
           user = form.save(commit=False)
           user.is_active = True
           user.is_passenger = True
           user.is_driver = False
           user.save()
           return redirect('/')
   else:
       form = RiderSignupForm()
   return render(request, 'registration/rider_signup.html', {'form': form})


@login_required
def driver_index(request):
    drivers = Driver.objects.all()
    user = request.user
    # print(drivers)
    return render(request,'registration/driver_inex.html', {"drivers":drivers, "user":user})