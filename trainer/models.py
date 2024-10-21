from django.db import models

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=255)
    nepali_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    qualification = models.CharField(max_length=255)
    tot = models.BooleanField(default=False)

    def __str__(self):
        return self.name