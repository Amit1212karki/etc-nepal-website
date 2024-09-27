from django.db import models
from trainer.models import *
from contract.models import *

# Create your models here.
class Batch(models.Model):
    name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    time = models.TimeField()
    seats = models.IntegerField()
    trainer = models.ManyToManyField(Trainer, related_name='batch_trainer')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='batch_contract')


    def __str__(self):
        return self.name