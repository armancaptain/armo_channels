from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "settings"
urlpatterns = [
    path('editprofile/', views.editprofile, name= "editprofile"),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='settings/change_password.html',success_url = '/'),name='change_password'),
    path('apps-and-websites/active/', views.active),
    path('apps-and-websites/expired/', views.expired),
    path('apps-and-websites/removed/', views.removed),
    path('emails-and-sms/', views.emails_and_sms),
    path('push-notification/', views.push_notification),
]
