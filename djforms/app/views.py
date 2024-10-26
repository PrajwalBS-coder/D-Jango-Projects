from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse as hr
from .models import *
# Create your views here.
def stu(re):
    s=StudentForm()
    if re.method=='POST':
        SDATA=StudentForm(re.POST)
        if SDATA.is_valid():
            s=StudentData.objects.get_or_create(name=re.POST.get('sname'),sid=re.POST.get('id'),email=re.POST.get('email'),url=re.POST.get('url'),address=re.POST.get('address'),password=re.POST.get('password'))
            if(s):
                return hr(str(SDATA.cleaned_data))
            else:
                hr("NOT ADDED TO DB")
            # print(re.POST.get('password'))
            # return hr(SDATA)
        else:
            return hr("WRONG")
    return render(re,'form.html',{'form':s})
