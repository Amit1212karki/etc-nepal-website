from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='video/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)