from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

from .models import Teams
from car_app.models import Cars

from contact_app.models import Contact_me
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError


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
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact_me(first_name=first_name, last_name=last_name, email=email, subject=subject, message=message)
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        form_email = email
        messages.success(request, 'Thanks for contact Us !')
        return redirect('contact')

        # if subject and message and form_email:
        #     try:
        #         send_mail(subject, message, form_email, [admin_email])
        #     except BadHeaderError:
        #         return HttpResponse('Invalid header found.')
        #     data.save()
        #     messages.success(request, 'Thanks for contact Us !')
        #     return redirect('contact')
        # else:
        #     return HttpResponse('Make sure all fields are entered and valid.')

    return render(request, 'pages/contact.html')
