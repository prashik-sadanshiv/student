from django.shortcuts import render
from .models import Student
# Create your views here.

def index(request):
  return render(request, 'index.html')

def register(request):

  dest1 = Student()
  dest1.fname = 'prashik'
  dest1.lname = 'sadanshiv'
  dest1.uname = 'prashik'
  dest1.age = '25'
  dest1.rollno = '101'
  return render(request, 'register.html', {'dest1':dest1})