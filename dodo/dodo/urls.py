from django.contrib import admin
from django.urls import path, include

from scheduler import views

urlpatterns = [
    path('', include('scheduler.urls')),
    path('admin/', admin.site.urls),
]