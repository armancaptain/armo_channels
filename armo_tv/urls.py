from django.urls import path
from . import views
from main.views import armo_tv

app_name = "armo_tv"
urlpatterns = [
    path('',views.create_armo_tv, name = "list"),
    path('create/',views.create_armo_tv, name = "create"),
    path('<slug>/',views.armo_tv, name= "detail"),
]
