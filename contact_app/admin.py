from django.contrib import admin
from .models import Inquiry_Contact


# Register your models here.

class contact_admin(admin.ModelAdmin):
    class Meta:
        model = Inquiry_Contact

    list_display = ['first_name', 'car_id', 'email', 'user_id']
    search_fields = ['first_name', 'email', 'user_id']
    list_display_links = ['first_name', 'car_id']
    list_filter = ['first_name', 'create_data']
    list_per_page = 25



admin.site.register(Inquiry_Contact, contact_admin)
