from django import forms
from . import models

class Create_text(forms.ModelForm):
    class Meta:
        model = models.text
        fields = ['title','slug','body',]