from django.db import models

# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField(("drag and drop an image here"), height_field=None, width_field=None, max_length=None)