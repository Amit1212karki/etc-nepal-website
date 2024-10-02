from django.db import models
from contract.models import *
from batch.models import *
from location.models import *
from datetime import date
# Create your models here.
class Trainee(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='trainee_contract')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='trainee_batch')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='trainee_province')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='trainee_district')
    palika = models.ForeignKey(Palika, on_delete=models.CASCADE, related_name='trainee_palika')
    ward_no = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    name = models.CharField(max_length=500)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth_ad = models.DateField()
    date_of_birth_bs = models.DateField()
    age = models.IntegerField()

    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
    ]

    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    ethnic_group = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    citizenship_no = models.CharField(max_length=100)
    issue_date = models.DateField()
    issue_district = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()
    qualification = models.CharField(max_length=255)
    image = models.FileField(upload_to='trainee/image/')
    citizenship_front_image = models.FileField(upload_to='trainee/citizenship_image/front/')
    citizenship_back_image = models.FileField(upload_to='trainee/citizenship_image/back/')
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return self.name


