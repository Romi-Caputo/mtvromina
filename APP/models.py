from django.db import models
from datetime import datetime   



class Familiares (models.Model):
    nombre= models.CharField(max_length=40)
    edad=models.IntegerField()
    fechanacimiento= models.CharField(max_length=10)
    
# Create your models here.
