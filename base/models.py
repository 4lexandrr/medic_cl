from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class User(AbstractUser):
#     pass


class Person(models.Model):
    """ Неудачная попытка """
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    years = models.DateField()
    polis = models.CharField(max_length=16)
    mobile_phone = models.CharField(max_length=11)
    email_p = models.EmailField()
    registration_address = models.CharField(max_length=200)
    fact_address = models.CharField(max_length=200)


class Client(models.Model):
    """ Класс клиентов (пользователи)"""
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    years = models.DateTimeField()
    policy = models.CharField(max_length=16)
    mobile_phone = models.CharField(max_length=11)
    email_p = models.EmailField()
    registration_address = models.CharField(max_length=200)
    fact_address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name


class Post(models.Model):
    """ Класс должностей работников медицинского учреждения """
    post = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.post


class Employees(models.Model):
    """ Класс работников медицинского учреждения """
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    mobile_phone = models.CharField(max_length=11)
    password = models.CharField(max_length=200)


    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name


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
    docror = models.ForeignKey(Employees, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True)
    attendes = models.ManyToManyField(Client)

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



