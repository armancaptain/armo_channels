from django.urls import path
from . import views

app_name = "explore"
urlpatterns = [
    path('', views.SearchView.as_view(), name='user_search'),
]
