from django.shortcuts import render

from django.views.generic import *
from .models import *


class ListOfStudent(ListView):
    model=Student
    context_object_name='objects_list'

class DetailOfStudent(DetailView):
    model=Student
    context_object_name='scobject'

class CreateStudent(CreateView):
    model=Student
    fields='__all__'

class UpdateStudent(UpdateView):
    model=Student
    fields='__all__'
    template_name='app/student_form.html'