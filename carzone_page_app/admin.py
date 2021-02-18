from django.contrib import admin
from .models import Teams

from django.utils.html import format_html


# Register your models here.

class TeamsAdmin(admin.ModelAdmin):
    class Meta:
        model = Teams

    def image_tag(self, obj):
        return format_html('<img src="{}" width="40" style="border-radius:50%" />'.format(obj.photo.url))

    image_tag.short_description = 'photo'

    list_display = ['id', 'image_tag', 'first_name', 'designation', 'create_data']
    list_display_links = ('id','image_tag', 'first_name')
    search_fields = ['create_data', 'first_name', 'last_name']
    list_filter = ['create_data', 'first_name']


admin.site.register(Teams, TeamsAdmin)
