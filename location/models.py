from django.db import models

# Create your models here.
class Province(models.Model):
    name = models.CharField(max_length=255)
    nepali_name = models.CharField(max_length=255,null=True)


    def __str__(self):
        return self.name

class District(models.Model):
    province_name = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province')
    name = models.CharField(max_length=255)
    nepali_name = models.CharField(max_length=255,null=True)


    def __str__(self):
        return self.name

class Palika(models.Model):
    district_name = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district')
    name = models.CharField(max_length=255)
    nepali_name = models.CharField(max_length=255,null=True)


    def __str__(self):
        return self.name
