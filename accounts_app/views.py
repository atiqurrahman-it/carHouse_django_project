from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def Login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ' successfully login ')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password incorrect !')
            return redirect('login')

    return render(request, 'accounts/login.html')


def Logout_page(request):
    logout(request)
    return redirect('/')


def Register_page(request):
    if request.method == 'POST':
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        conform_password = request.POST["confirm_password"]

        if password == conform_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User name already taken  !')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email  already taken  !')
                return redirect('register')
            else:
                x = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                             password=password, )
                x.save()
                messages.success(request, ' successfully register   !')
                return redirect('login')


        else:
            messages.error(request, 'Password DoesNot match !')
            return redirect('register')

    return render(request, 'accounts/register.html')
    # messages.error(request, 'Email or password invalid !')


def Dashboard_page(request):
    return render(request, 'accounts/Dashboard.html')
