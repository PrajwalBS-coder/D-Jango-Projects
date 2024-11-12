from django.shortcuts import render
from django.http import HttpResponse as hr
# Create your views here.
from .forms import *


def Registration(re):
    if re.method=='POST':
        return hr (str(UserForm(re.POST))+str(Profile_form(re.POST)))
    return render(re,'Registration.html',{'uform':UserForm(),'pform':Profile_form()})