from django.shortcuts import render
from .forms import *
from django.http import HttpResponse as hr


# Create your views here.
def InsertStudent(re):
    if re.method=='POST':
        data=StudentForm(re.POST)
        if data.is_valid():
            data.save()
            hr('Ok')
        else:
            hr('Error')
    return render(re,'form.html',{'form':StudentForm()})

def filter(re):
    return render(re,'filter.html',{'data':"AminA Is Legend"})
