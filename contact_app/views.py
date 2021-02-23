from django.shortcuts import render, redirect, HttpResponse
from .models import Inquiry_Contact
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


# Create your views here.

def inquiry_model(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        first_name = request.POST['first_name']
        second_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        location = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            hsa_connect = Inquiry_Contact.objects.all().filter(user_id=user_id, car_id=car_id)
            if hsa_connect:
                messages.success(request, 'your are already  request !!')
                return redirect('/car_app/single_page/' + car_id)

        contact = Inquiry_Contact(user_id=user_id, car_id=car_id, first_name=first_name,
                                  last_name=second_name, customer_need=customer_need, car_title=car_title,
                                  city=location, state=state, email=email, phone=phone, message=message)
        admin_info = User.objects.get(is_superuser=True)
        admin_mail = admin_info.email
        to_mail = email
        send_mail(
            'New car Inquiry ',
            'you have a now inquiry for tha car' + car_title + '.please login to your admin panel for more info.',
            admin_mail,
            [to_mail],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'your request has been submitted. Thanks for the request')
        return redirect('/car_app/single_page/' + car_id)
