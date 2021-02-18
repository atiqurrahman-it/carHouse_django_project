from django.shortcuts import render, HttpResponse


# Create your views here.

def Car(request):
    return render(request,'cars/cars.html')
