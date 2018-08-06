from django.shortcuts import render
from .forms import PassProfileForm, PassLocationForm


# Create your views here.

def passprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = PassProfileForm(request.POST, request.FILES)
        if form.is_valid():
            passenger = form.save(commit=False)
            passenger.user = current_user
            passenger.save()
    else:
        form = PassProfileForm()
    return render(request,'profile/passprofile.html',{"form":form})

def passlock(request):
    current_user = request.user
    if request.method == 'POST':
        form = PassLocationForm(request.POST,request.FILES)
        if form.is_valid():
            location = form.save(commit=False)
            location.user = current_user
            location.save()
    else:
        form = PassLocationForm()
    return render(request,'profile/location.html',{"form":form})
