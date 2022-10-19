from dataclasses import Field
import datetime
from doctest import DocTestRunner
from operator import mod
from tabnanny import verbose
from django.utils import timezone
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import * 



# Create your models here.


class Post(models.Model):
    """ Класс должностей работников медицинского учреждения """
    post = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.post


telephone = RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class User(AbstractUser):
    class Types(models.TextChoices):
        USER = 'USER', 'User'
        ADMIN = 'ADMIN', 'Admin'
    

    username = models.CharField(max_length=50, default="Test")
    type = models.CharField(max_length=255, choices=Types.choices, default=Types.USER)
    
    first_name = models.CharField(max_length=255, default="Test")
    middle_name = models.CharField(max_length=50, default="Test")
    second_name = models.CharField(max_length=50, default="Test")
    years = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1900), max_value_current_year])
    email = models.EmailField(unique=True, default="Test")
    polis = models.CharField(max_length=16, default="Test")
    mobile_phone = models.CharField(max_length=18, validators=[telephone, MaxLengthValidator], default="Test")
    registration_address = models.CharField(max_length=200, default="Test")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    
    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name


class UserManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.USER)


class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)


class Client(User):
    objects = UserManager()

    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.USER
        return super().save(*args, **kwargs)


class Admin(User):
    objects = AdminManager()

    class Meta:
        proxy = True
    

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.ADMIN
        return super().save(*args, **kwargs)


class Venue(models.Model):
    """ Класс адресов , в которые может быть записано пациент """
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Events(models.Model):
    """ Класс событий, на которые может быть записан пациент """
    name = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # venue = models.CharField(max_length=50)
    # manager = models.CharField(max_length=50)
    # docror = models.ForeignKey(Employees, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True)
    attendes = models.ManyToManyField(Client)

    def __str__(self):
        return self.name

    
class Tests(models.Model):
    """ Класс тестов, на которые может быть записан пациент """
    name = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Type_of_diagnoses(models.Model):
    """ Класс диагнозов для удобной подстановки"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Visits(models.Model):
    name = models.ForeignKey(Events, on_delete=models.CASCADE, blank=True)
    visit_date = models.DateTimeField()
    description = models.TextField(blank=True)





