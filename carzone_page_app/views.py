from django.shortcuts import render, HttpResponse

from .models import Teams
from car_app.models import Cars


# Create your views here.

def Home_page(request):
    total_team = Teams.objects.all()
    features_car = Cars.objects.order_by('-create_data').filter(is_features=True)
    total_car = Cars.objects.order_by('-create_data')[:9]
    # search_fields = Cars.objects.values('model', 'city', 'year', 'body_style') # is this way problem  dublicatvalu
    model_search = Cars.objects.values_list('model', flat=True).distinct()
    city_search = Cars.objects.values_list('city', flat=True).distinct()
    year_search = Cars.objects.values_list('year', flat=True).distinct()
    body_style_search = Cars.objects.values_list('body_style', flat=True).distinct()
    data = {
        "total_team": total_team,
        "features_car": features_car,
        "total_car": total_car,
        # "search_fields": search_fields,
        "model_search": model_search,
        "city_search": city_search,
        "year_search": year_search,
        "body_style_search": body_style_search,
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
