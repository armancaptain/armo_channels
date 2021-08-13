from django.urls import path
from django.contrib.auth import views
from .views import singup
urlpatterns = [
    path('singup/', singup),
    path('login/', views.LoginView.as_view(template_name='accounts/login.html'), name="login")
]