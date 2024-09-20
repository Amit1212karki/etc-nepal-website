from django.db import models

# Create your models here.

class SuccessHistory(models.Model):
    title = models.CharField(max_length=255)  
    description = models.TextField()  
    number = models.IntegerField() 
    suffix = models.CharField(max_length=10, blank=True, null=True)  
    is_active = models.BooleanField(default=True) 
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
