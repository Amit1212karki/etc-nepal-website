from django.db import models
from ckeditor.fields import RichTextField

class Course(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    description = RichTextField()  # Use CKEditor for rich text
    image = models.ImageField(upload_to='course_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
