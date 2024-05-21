from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,"index.html")

def second(request):
    return render(request,"login.html")

def adarsh(request):
    return render(request,"register.html" )

def fourth(request):
    return render(request,"userprofile.html")

def fifth(request):
    return render(request,"booking.html")