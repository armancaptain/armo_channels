from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Subject(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    profile = models.ImageField(default = "/media/2.jpg")
    bio = models.CharField(max_length=1000)
    website = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=40)
    gender = models.CharField(max_length=7)

user = get_user_model()

User.profile = property(lambda u: Subject.objects.get_or_create(user=u)[0])