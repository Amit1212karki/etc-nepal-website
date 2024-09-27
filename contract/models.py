from django.db import models

# Create your models here.
class Contract(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    donation_by = models.CharField(max_length=255)

    def __str__(self):
        return self.name