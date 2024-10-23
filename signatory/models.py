from django.db import models

# Create your models here.
class Signatory(models.Model):
    name = models.CharField(max_length=255)
    nepali_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    nepali_designation = models.CharField(max_length=255)
    institution = models.CharField(max_length=255,null=True,blank=True)
    nepali_institution = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
