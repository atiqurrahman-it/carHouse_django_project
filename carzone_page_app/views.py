from django.shortcuts import render, HttpResponse

from .models import Teams


# Create your views here.

def Home_page(request):
    total_team = Teams.objects.all()
    data = {
        "total_team": total_team,
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
