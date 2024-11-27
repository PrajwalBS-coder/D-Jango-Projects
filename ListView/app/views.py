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

class SchoolDetails(DetailView):
    model=Ischool
    # template_name="detailed.html"

class CreateSchool(CreateView):
    model=Ischool
    fields='__all__'

class UpdateSchool(UpdateView):
    model=Ischool
    fields='__all__'

class DeletVSchool(DeleteView):
    model=Ischool
    # context_object_nam='schoolobj'
 