from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def Login_page(request):
    return render(request, 'accounts/login.html')


def Logout_page(request):
    return redirect('/')


def Register_page(request):
    return render(request, 'accounts/register.html')


def Dashboard_page(request):
    return render(request, 'accounts/Dashboard.html')
