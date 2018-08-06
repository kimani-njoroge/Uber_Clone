from django.shortcuts import render
from .forms import DriverProfileForm,CarProfileForm

# Create your views here.
def driveprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = DriverProfileForm(request.POST,request.FILES)
        if form.is_valid():
            driver = form.save(commit=False)
            driver.user = current_user
            driver.save()
    else:
        form = DriverProfileForm()
    return render(request,'profile/driverprof.html',{"form":form})