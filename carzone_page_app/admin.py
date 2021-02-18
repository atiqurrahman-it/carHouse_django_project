from django.contrib import admin
from .models import Teams


# Register your models here.

class TeamsAdmin(admin.ModelAdmin):
    class Meta:
        model = Teams


admin.site.register(Teams, TeamsAdmin)
