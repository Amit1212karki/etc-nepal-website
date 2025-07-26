from django.db import models
# Create your models here.
from io import BytesIO
from django.core.files import File


class Certificate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to='backgrounds/', blank=True)
    qr_code_image = models.ImageField(upload_to='qr_codes/', blank=True, editable=False)
