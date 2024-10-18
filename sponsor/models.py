from django.db import models

# Create your models here.

class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sponsor_images/')