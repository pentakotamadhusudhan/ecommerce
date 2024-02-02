from django.db import models


class ImageModel(models.Model):
    Image = models.ImageField()
    objects = models.Manager
# Create your models here.
