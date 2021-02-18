from django.contrib import admin
from .models import Cars

from django.utils.html import format_html

# Register your models here.

class CarsAdmin(admin.ModelAdmin):
    class Meta:
        model = Cars

    def image_tag(self, obj):
        return format_html('<img src="{}" width="40" style="border-radius:50%" />'.format(obj.car_photo.url))

    image_tag.short_description = 'photo'

    list_display = ['id', 'image_tag', 'car_title', 'create_data']
    list_display_links = ('id', 'image_tag', 'car_title')
    search_fields = ['create_data', 'car_title', 'id']
    list_filter = ['create_data', 'car_title']


admin.site.register(Cars, CarsAdmin)
