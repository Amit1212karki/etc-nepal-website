from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)