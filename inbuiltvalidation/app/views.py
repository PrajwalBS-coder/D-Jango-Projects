from django.shortcuts import render
from .forms import *
from django.http import HttpResponse as hr
# Create your views here.
def Insert(re):
    if re.method=='POST':
        data=AllinOneForm(re.POST)
        if data.is_valid():
            data.save()
        else:
            hr('Wrong ONe')
    return render(re,'AllinOne.html',{'form':AllinOneForm()})