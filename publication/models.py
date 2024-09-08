from django.db import models

# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(max_length=500)
    long_description = models.TextField()
    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)

    def __str__(self):
        return self.title
