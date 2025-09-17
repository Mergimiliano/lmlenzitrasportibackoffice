from django.db import models

# Create your models here.
class Tractor(models.Model):
    plate = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.plate
    
class Trailer(models.Model):
    plate = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.plate