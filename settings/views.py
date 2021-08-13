from django.shortcuts import render
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponseRedirect

def editprofile(request):
    userup = forms.UpdateUser(request.POST or None, instance=request.user)
    profileup = forms.UpdateProfile(request.POST or None, instance=request.user.profile)
    if request.method == 'POST':
        profileup = forms.UpdateProfile(request.POST or None, instance=request.user.profile)
        if profileup.is_valid():
            profileup.save()
            userup = forms.UpdateUser(request.POST or None, instance=request.user)
            if userup.is_valid():
                user = userup.save(commit=False)
                user.first_name == request.POST['first_name']
                user.save()
            return HttpResponseRedirect('Chat : home')
    else:
        user = request.user
        profile = user.profile
        userup = forms.UpdateUser(instance=user)
        profileup = forms.UpdateProfile(instance=profile)

    args = {
        'userup': userup,
        'profileup': profileup,
    }
    return render(request, 'settings/update_profile.html', args)
    
def active(request):
    return render(request, 'settings/apps-and-websites.html')

def expired(request):
    return render(request, 'settings/expierd.html')

def removed(request):
    return render(request, 'settings/removed.html')

def emails_and_sms(request):
    return render(request, 'settings/emails-and-sms.html')

def push_notification(request):
    return render(request, 'settings/push-notification.html')