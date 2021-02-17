from django.shortcuts import render, HttpResponse


# Create your views here.

def Home_page(request):
    return render(request, 'index.html')
