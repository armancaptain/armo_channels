from django import forms
from . import models

class search(forms.ModelForm):
    class Meta:
        model = models.search
        fields = ['search']