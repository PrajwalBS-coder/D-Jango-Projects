from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from app.models import *

class SchholList(ListView):
    model=Ischool
    context_object_name='abc'

class StudentList(ListView):
    model=Student
    context_object_name='stu'
    
    