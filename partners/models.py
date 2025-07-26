from django.db import models

# Create your models here.
class Partner(models.Model):
    name = models.TextField()
    image = models.FileField(upload_to='partner_images/')
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    