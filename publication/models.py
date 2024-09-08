from django.db import models

# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    long_description = models.CharField(max_length=2000)
    pdf = models.FileField(upload_to='pdfs/' , blank=True, null=True)
