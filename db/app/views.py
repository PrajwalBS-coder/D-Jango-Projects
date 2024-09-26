from django.shortcuts import render
from app.models import *
from django.http import HttpResponse as hr
# Create your views here.

def op(re):
    empdet=emp.objects.all()
    print(empdet)
    return render(re,'op.html',{'empdet': empdet})
# def insert(re):
#     # tn=input()
#     # name=input()
#     # u=input()
#     # em=input()
#     # au=input()
#     # da=input()
#     l=list(map(str,input('Enter Topic Name Url Email Author Date').split()))
#     # TO=topic.objects.get_or_create(topic_name=tn)
#     # WO=webpage.objects.get_or_create(topic_name=TO[0],name=name,url=u,email=em)
#     # AR=access.objects.get_or_create(name=WO[0],author=au,date=da)
#     TO=topic.objects.get_or_create(topic_name=l[0])
#     WO=webpage.objects.get_or_create(topic_name=TO[0],name=l[1],url=l[2],email=l[3])
#     AR=access.objects.get_or_create(name=WO[0],author=l[4],date=l[5])
#     if(AR[1]):
#         return hr('Created')
#     else:
#         return hr("It's There Bro")
    
# def cap(re):
#     Existting_country=country.objects.all()
#     # print(Existting_country)
#     c=int(input('Chose 1 for Editing Counries Captial 2 for Adding New Contry'))
#     if c==1:
#         ci=int(input('You can chose any country from 0 to '+str(len(Existting_country)-1)))
#         CO=country.objects.get_or_create(country_name=Existting_country[ci])
#     elif c==2:
#         cn=input(' Add New Contry')
#         CO=country.objects.get_or_create(country_name=cn)

#     cp=input('CAPNAME')
#     # if(type(int(cn))):
#     #     CO=country.objects.get_or_create(country_name=Existting_country[int(cn)]) 
#     # else: 
#     #     CO=country.objects.get_or_create(country_name=cn)
#     CPO=capital.objects.get_or_create(country_name=CO[0],capital_name=cp)
#     if CPO[1]:
#         return hr('Done Man')
#     else:
#         return hr('Country Is There i Think')
    
# def cap2(re):
#     cn=input('Cname')
#     CO=country.objects.get_or_create(country_name=cn)
#     if CO[1]:
#         return hr('Done Man')
#     else:
#         return hr('WrOng')
    
# def emp(re):
#     d=dept.objects.all()
#     print(d)
#     dno=input('')
def insert(re):
    tn=input()
    name=input()
    u=input()
    em=input()
    TO=topic.objects.get(topic_name=tn)
    WO=webpage.objects.get_or_create(topic_name=TO,name=name,url=u,email=em)
    return hr('Created')
