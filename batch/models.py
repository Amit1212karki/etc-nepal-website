from django.db import models
from trainer.models import *

# Create your models here.
class Batch(models.Model):
    name = models.CharField(max_length=255)
    contract = models.TextField()
    duration = models.CharField(max_length=255)
    time = models.TimeField()
    seats = models.IntegerField()
    trainer = models.ManyToManyField(Trainer, related_name='batch_trainer')

    def __str__(self):
        return self.name