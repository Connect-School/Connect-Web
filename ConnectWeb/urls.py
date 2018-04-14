from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('public.urls')),
    path('api/', include("api.urls")),
    path('core/', include('core.urls')),
    path('escola/', include('escola.urls')),
    path('secretaria/', include('secretaria.urls')),
    path('dired/', include('dired.urls')),
]
