"""DjangoChannels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views
from Chat.views import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('plus/', views.plus),
    path('posts/', views.posts, name='list'),
    path('armo_tv/', views.armo_tv),
    #path('accounts/<slug>',views.Subject, name = "accounts"), 

    path('chat/', include('Chat.urls')),
    path('business/', include('business.urls')),
    path('articles/' , include('articles.urls')),
    path('armo_tv/' , include('armo_tv.urls')),
    path('text/' , include('text.urls')),
    path('explore/' , include('explore.urls')),
    path('settings/' , include('settings.urls')),
    path('accounts/' , include('accounts.urls')),


]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
