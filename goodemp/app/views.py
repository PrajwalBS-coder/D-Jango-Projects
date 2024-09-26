from django.shortcuts import render
from app.models import *
from django.http import HttpResponse as hr
# Create your views here.
def op(re):
    emp=Emp.objects.all()
    return render(re,'op.html',{'emp':emp})

def insert(re):
    eno=input('Enter eno')
    na=input('Enter name')
    job=input('Enter job')
    da=input('Enter date')
    sal=input('Salary')
    dno=input('Enter dno')
    mgr=input('Enter mgr')
    com=input('Enter commission')
    DO=Dept.objects.get(deptno=dno)
    if DO:
        MO=Emp.objects.get(eno=mgr)
        if MO:
            EO=Emp.objects.get_or_create(eno=eno,ename=na,job=job,sal=sal,dno=DO,mgr=MO,comm=com)
            if EO[1]:
                return hr('Created Man')
            else:
                return hr('Not Created')
        else:
            EO=Emp.objects.get_or_create(eno=eno,ename=na,job=job,sal=sal,dno=DO,mgr=MO,comm=com)
            if EO[1]:
                return hr("Created BRo")
            else:
                return hr("NOT possible")
    else:
        return hr("Department Doenot exist")

def insert2(re):
    eno=input('Enter eno')
    na=input('Enter name')
    job=input('Enter job')
    da=input('Enter date')
    sal=input('Salary')
    dno=input('Enter dno')
    mgr=input('Enter mgr')
    com=input('Enter commission')
    DO=Dept.objects.filter(deptno=dno)
    if DO:
        MO=Emp.objects.filter(eno=mgr)
        if MO:
            EO=Emp.objects.get_or_create(eno=eno,ename=na,job=job,sal=sal,dno=DO[0],mgr=MO[0],comm=com)
            if EO[1]:
                return hr('Created Man')
            else:
                return hr('Not Created')
        else:
            EO=Emp.objects.get_or_create(eno=eno,ename=na,job=job,sal=sal,dno=DO[0],mgr=MO[0],comm=com)
            if EO[1]:
                return hr("Created BRo")
            else:
                return hr("NOT possible")
    else:
        return hr("Department Doenot exist")

