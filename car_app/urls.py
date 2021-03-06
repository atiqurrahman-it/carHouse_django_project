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
    path('car/', views.Car, name='car'),
    path('single_page/<int:id>/', views.Car_details, name='car_details'),
    path('search/', views.Search, name="search"),

]
