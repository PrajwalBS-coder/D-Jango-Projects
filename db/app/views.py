from django.shortcuts import render
from app.models import *
from django.http import HttpResponse as hr
# Create your views here.

def op(re):
    empdet=emp.objects.all()
    print(empdet)
    return render(re,'op.html',{'empdet': empdet})
def insert(re):
    tn=input()
    name=input()
    u=input()
    em=input()
    au=input()
    da=input()
    TO=topic.objects.get_or_create(topic_name=tn)
    WO=webpage.objects.get_or_create(topic_name=TO[0],name=name,url=u,email=em)
    AR=access.objects.get_or_create(name=WO[0],author=au,date=da)
    if(AR[1]):
        return hr('Created')
    else:
        return hr("It's There Bro")
    
def cap(re):
    cn=input('Cname')
    cp=input('CAPNAME')
    CO=country.objects.get_or_create(country_name=cn)
    CPO=capital.objects.get_or_create(country_name=CO[0],capital_name=cn)
    if CPO[1]:
        return hr('Done Man')
    else:
        return hr('Country Is There i Think')
    
def cap2(re):
    cn=input('Cname')
    CO=country.objects.get_or_create(country_name=cn)
    if CO[1]:
        return hr('Done Man')
    else:
        return hr('WrOng')
    
def emp(re):
    d=dept.objects.all()
    print(d)
    dno=input('')
