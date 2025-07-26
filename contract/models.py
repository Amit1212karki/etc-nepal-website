from django.db import models

# Create your models here.
class Contract(models.Model):
    name = models.CharField(max_length=255)
    nepali_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    nepali_location = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    nepali_occupation = models.CharField(max_length=255)
    donation_by = models.CharField(max_length=255)
    nepali_donation_by = models.CharField(max_length=255)

    def __str__(self):
        return self.name