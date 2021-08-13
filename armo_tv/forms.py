from django import forms
from . import models

class Create_armo_tv(forms.ModelForm):
    class Meta:
        model = models.armo_tv
        fields = ['title','slug','body','video','cover','extension']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('name', 'email', 'body')