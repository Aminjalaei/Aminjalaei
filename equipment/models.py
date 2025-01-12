from django.db import models

# Create your models here.
from django.db import models

class Personnel(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(Personnel, on_delete=models.CASCADE)

