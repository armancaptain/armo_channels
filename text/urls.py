from django.urls import path
from . import views
from main.views import text

app_name = "text"
urlpatterns = [
    path('', text, name = "list"),
    path('create/',views.create_text, name = "create"),
    path('<slug>',views.text, name= "detail"),
]
