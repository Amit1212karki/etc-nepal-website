from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)
    
