from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def armo_tv(request, slug):
    # return HttpResponse(slug)
    armo_tv = models.armo_tv.objects.get(slug=slug)
    return render(request, 'armo_tv/article_detail.html',{'armo_tv': armo_tv})

@login_required(login_url = "/accounts/login")
def create_armo_tv(request):
    if request.method == 'POST':
        form = forms.Create_armo_tv(request.POST,request.FILES)
        if form.is_valid:
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('armo_tv:list')
    else:
        form = forms.Create_armo_tv()
    return render(request , 'armo_tv/create_article.html',{'form':form})
