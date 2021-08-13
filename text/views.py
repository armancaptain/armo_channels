from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def text(request, slug):
    # return HttpResponse(slug)
    text = models.text.objects.get(slug=slug)
    print(text)
    return render(request, 'text/article_detail.html',{'text':text})

@login_required(login_url = "/accounts/login")
def create_text(request):
    if request.method == 'POST':
        form = forms.Create_text(request.POST,request.FILES)
        if form.is_valid:
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('text:list')
    else:
        form = forms.Create_text()
    return render(request , 'text/create_article.html',{'form':form})
