from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse as hr

# Create your views here.
def stu(re):
    s=StudentForm()
    if re.method=='POST':
        SDATA=StudentForm(re.POST)
        if SDATA.is_valid():
            return hr(str(SDATA.cleaned_data))
        else:
            return hr("WRONG")
    return render(re,'form.html',{'form':s})
