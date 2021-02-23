from django.db import models


# Create your models here.

class Inquiry_Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    car_id = models.IntegerField()
    car_title = models.CharField(max_length=200)
    customer_need = models.CharField(max_length=200)
    email = models.EmailField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField()
    user_id = models.IntegerField()
    create_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
