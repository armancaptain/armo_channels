from django.shortcuts import render ,redirect ,HttpResponse ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def singup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = UserCreationForm()
    return render(request ,'accounts/singup.html',{'form':form}) 