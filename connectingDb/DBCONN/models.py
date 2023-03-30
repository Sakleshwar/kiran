from django.db import models
# from DBCONN.models import *

# Create your models here.

class Apartment(models.Model) : 
    roomSize = models.IntegerField(max_length=4)
    noofWindows = models.IntegerField(max_length=3)
    isMetro = models.BooleanField(default=False)

class Villa(models.Model):
    noOfRooms = models.IntegerField(max_length=5)
    carpetArea = models.IntegerField(max_length=150)
    isMetro = models.BooleanField(default=False)

class Employeedetails(models.Model):
    empname = models.CharField(max_length=20)
    emp_age = models.IntegerField(max_length=2)
    emp_id = models.CharField(max_length=8)
    emp_department = models.CharField(max_length=10)
    
class Restaurant(models.Model):
    Menu = models.CharField(max_length=50)
    noOfTable = models.IntegerField(max_length=8)
    section = models.CharField(max_length=5)
    price = models.FloatField(max_length=4)


