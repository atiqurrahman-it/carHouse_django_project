"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home_page, name='homepage'),
    path('about/', views.About_page, name='about'),
    path('services/', views.Services_page, name='services'),
    path('contact/', views.Contact_page, name='contact'),
]
