from django.db import models

# Create your models here.

class Student(models.Model):

  fname = models.CharField(max_length=100)
  lname = models.CharField(max_length=100)
  uname = models.CharField(max_length=100)
  age = models.IntegerField()
  rollno = models.IntegerField()