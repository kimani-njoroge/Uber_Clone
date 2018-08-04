from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import DriverSignupForm

User = get_user_model()
# Create your views here.
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
    return render(request,'registration/driver_signup.html',{"form":form})