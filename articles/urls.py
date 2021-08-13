from django.urls import path
from . import views
from main.views import posts

app_name = "articles"
urlpatterns = [
    path('',views.create_article, name = "list"),
    path('create/',views.create_article, name = "create"),
    path('<slug>',views.article_detail, name= "detail"),
]
