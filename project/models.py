from django.db import models

# Create your models here.

class Project(models.Model):
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Complete', 'Complete')
    ]
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='project_image/')
    description = models.TextField()
    partner = models.CharField(max_length=255)
    project_location = models.CharField(max_length=255)
    project_duration = models.IntegerField()
    result_and_activaties = models.CharField(max_length=255)
    status = models.TextField(max_length=50 , choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
