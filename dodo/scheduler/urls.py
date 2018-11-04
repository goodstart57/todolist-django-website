from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/post/', views.post_schedule, name='post_schedule'),
]