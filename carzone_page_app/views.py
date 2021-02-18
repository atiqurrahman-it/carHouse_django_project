from django.shortcuts import render, HttpResponse

from .models import Teams
from car_app .models import Cars


# Create your views here.

def Home_page(request):
    total_team = Teams.objects.all()
    features_car = Cars.objects.order_by('-create_data').filter(is_features=True)
    total_car = Cars.objects.order_by('-create_data')
    data = {
        "total_team": total_team,
        "features_car": features_car,
        "total_car": total_car,
    }
    return render(request, 'pages/index.html', data)


def About_page(request):
    total_team = Teams.objects.all()
    data = {
        "total_team": total_team,
    }
    return render(request, 'pages/about.html', data)


def Services_page(request):
    return render(request, 'pages/services.html')


def Contact_page(request):
    return render(request, 'pages/contact.html')
