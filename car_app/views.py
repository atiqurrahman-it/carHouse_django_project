from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Cars


# Create your views here.

def Car(request):
    t_car = Cars.objects.order_by('-create_data')
    data = {
        "t_car": t_car,
    }
    return render(request, 'cars/cars.html', data)


def Car_details(request, id):
    single_car_details = get_object_or_404(Cars, id=id)
    data = {
        "car_details": single_car_details
    }
    return render(request, 'cars/car_details.html', data)
