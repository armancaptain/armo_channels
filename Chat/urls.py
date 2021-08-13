from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('index/', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]