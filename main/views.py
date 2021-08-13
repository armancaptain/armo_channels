from django.shortcuts import render ,redirect ,HttpResponse ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.utils.safestring import mark_safe
import json
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from articles.models import Article 
from armo_tv import models 
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url="login")
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url="login")
def plus(request):
    return render(request, 'main/plus.html')

@login_required(login_url="login")
def armo_tv(request):
    import os
    articles = models.armo_tv.objects.all().order_by('-date')
    args = {'articles':articles}
    return render(request, 'main/armo_tv.html', args)
    

@login_required(login_url="login")
def text(request):
    import os
    articles = Article.objects.all().order_by('-date')
    args = {'articles':articles}
    return render(request, 'main/text_post.html')

@login_required(login_url="login")
def posts(request):
    import os
    articles = Article.objects.all().order_by('-date')
    args = {'articles':articles}
    return render(request, 'main/post.html', args)