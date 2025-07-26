from django.db import models

# Create your models here.

class TeamCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='team_image/')
    designation = models.CharField(max_length=255)
    category = models.ForeignKey(TeamCategory, on_delete=models.CASCADE)


