from django.shortcuts import render
from .models import *
from django.http import *
# Create your views here.
def insert(re):
    name=input("ENTER NAME")
    sex=input("ENTER gender")
    schol=input("ENTER School")
    so=school.objects.get(name=schol)
    if so:
        sto=student.objects.get_or_create(name=name,gender=sex,school_name=so)
        if sto:
            return HttpResponse("OK DONE")

    return HttpResponse("!OK")

def update(re):
    student.objects.filter(id=1).update(school_name='ABC')
    return render(re,'disp.html',{'d':student.objects.all()})
def delete(re):
    student.objects.filter(id=1).delete()
    return render(re,'disp.html',{'d':student.objects.all()})
def insert_form(re):
    obj=school.objects.all()
    if re.method =='POST':
        na=re.POST['na']
        ge=re.POST['ge']
        sc=re.POST['sc']
        so=school.objects.get(name=sc)
        stu=student.objects.get_or_create(name=na,gender=ge,school_name=so)
        if stu:
            return render(re,'disp.html',{'d':student.objects.all()})

    return render(re,'insertform.html',{'d':obj})