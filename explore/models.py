from django.db import models
from django.contrib.auth.models import User

class search(models.Model):
    search = models.CharField(max_length = 200)

    def __str__(self):
        return self.search
