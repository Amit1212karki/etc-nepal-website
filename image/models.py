from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=255)
    cover = models.FileField(upload_to='image_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Model to store multiple images related to a single Image
class Images(models.Model):
    image = models.ForeignKey(Image, related_name='multiple_images', on_delete=models.CASCADE)
    images = models.FileField(upload_to='image_multiple_images/')

    def __str__(self):
        return f"{self.image.title or 'Untitled'} Image"