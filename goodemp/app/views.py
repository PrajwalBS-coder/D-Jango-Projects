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
    DO=Dept.objects.get(deptno=dno)#if department no doesnot exist it'll throw error snd stops the execution
    if DO:
        MO=Emp.objects.get(eno=mgr)#if Manager no doesnot exist it'll throw error snd stops the execution
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
    com=(input('Enter commission'))
    if(com):
        com=int(com)
    else:
        com=None
    DO=Dept.objects.filter(deptno=dno)#if department no doesnot exist we can handle ther error by reponsing an HttpResponse to Web Page That'y it's comparitively better than get method
    if DO:
        if(mgr):
            MO=Emp.objects.filter(eno=int(mgr))
            if MO:
                EO=Emp.objects.get_or_create(eno=eno,ename=na,job=job,hiredate=da,sal=sal,dno=DO[0],mgr=MO[0],comm=com)
                if EO[1]:
                    return hr('Created Man')
                else:
                    return hr('Not Created')
        else:
            EO=Emp.objects.get_or_create(eno=eno,ename=na,job=job,hiredate=da,sal=sal,dno=DO[0],comm=com)
            if EO[1]:
                return hr("Created BRo")
            else:
                return hr("NOT possible")
    else:
        return hr("Department Doenot exist")

def disp(re):
    columns1=[field.name for field in Emp._meta.get_fields()][1::]
    columns2=[field.name for field in Dept._meta.get_fields()][1::]
    columns=columns2+columns1
    data=Dept.objects.prefetch_related('emp_set').all()
    return render(re,'emp_dept.html',{'columns':columns,'data':data})
 
