from django.shortcuts import render

from django.views.generic import ListView
from .models import *


class ListOfStudent(ListView):
    model=Student
    context_object_name='objects_list'
