
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('carzone_page_app.urls')),
                  path('car_app/', include('car_app.urls')),
                  path('accounts_app/', include('accounts_app.urls')),
                  path('contact_app/', include('contact_app.urls')),
                  # path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('accounts/', include('allauth.urls')),
              ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
