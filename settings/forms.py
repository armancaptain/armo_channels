from django import forms
from django.contrib.auth.models import User
from .models import Subject

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['slug', 'profile', 'bio', 'website', 'phone_number', 'gender']


class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This is not your email')

        return email
