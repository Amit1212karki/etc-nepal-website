from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='document_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
