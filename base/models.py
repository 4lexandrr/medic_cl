from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    years = models.DateField()
    polis = models.CharField(max_length=16)
    mobile_phone = models.CharField(max_length=11)
    email_p = models.CharField(max_length=100)
    registration_address = models.CharField(max_length=200)
    fact_address = models.CharField(max_length=200)
