from django.shortcuts import render, HttpResponse


# Create your views here.

def Home_page(request):
    return render(request, 'pages/index.html')


def About_page(request):
    return render(request, 'pages/about.html')

def Services_page(request):
    return render(request, 'pages/services.html')

def Contact_page(request):
    return render(request, 'pages/contact.html')