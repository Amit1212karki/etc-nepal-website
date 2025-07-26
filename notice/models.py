from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.FileField(upload_to='notice_image/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

