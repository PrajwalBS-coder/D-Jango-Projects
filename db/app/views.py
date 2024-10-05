from django.shortcuts import render
from app.models import *
from django.http import HttpResponse as hr
from django.db.models.functions import Length
from django.db.models import Q
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
def insert_topic(re):
    tn=input()
    TO=topic.objects.get_or_create(topic_name=tn)
    if(TO[1]):
        return render(re,'op2.html',{'topics':topic.objects.all()})
    else:
        return hr("It's There Bro")

def insert_webpage(re):
    tn=input()
    name=input()
    u=input()
    em=input()
    TO=topic.objects.filter(topic_name=tn)
    if TO:
        WO=webpage.objects.get_or_create(topic_name=TO[0],name=name,url=u,email=em)
        if WO:

            return render(re,'webpage.html',{'webpage':webpage.objects.all()})
        else:
            return hr('Webgage NOt Created')
    else:
        return hr("TOPIC NAHI HAI BHAI")


# ONE TEMPLATE FOR ALL THE WEB PAGE

def topi(re):
    # columns=[field.name for field in topic._meta.get_fields()]
    columns1=[field.name for field in emp._meta.get_fields()]
    columns2=[field.name for field in dept._meta.get_fields()][1::]
    columns=columns1+columns2
    # columns=columns[1::]#it;ll be usefull in topic model only ,webpage._meta.get_fields()
    # data=topic.objects.all()
    # data=webpage.objects.values()

    # # Create a list of rows, where each row is a dictionary mapping column names to their values
    # data_rows = []
    # for obj in data:
    #     row = {}
    #     for column in columns:
    #         row[column] = getattr(obj, column)  # Dynamically get the value of each field
    #     data_rows.append(row)
    # data = capital.objects.values().order_by("capital_name")
    # data = access.objects.filter(date__range=["1999-01-01", "2024-01-31"]).order_by('date')#range working fine
    # data = emp.objects.filter(eno__lt=100).order_by('ename')#lt working fine
    # data = emp.objects.filter(eno__gt=100).order_by('ename')
    # data = emp.objects.filter(eno__lte=102).order_by('ename')
    # data = emp.objects.filter(eno__gte=90).order_by('ename')
    # data = access.objects.filter(date__month='04')
    # data = access.objects.filter(date__year='2002')
    # data = access.objects.filter(date__day="19")#it'll print day of the month
    # data = topic.objects.filter(topic_name__in=('Songs','Mini Series'))
    # data = topic.objects.filter(topic_name__contains='e')
    # data = topic.objects.filter(topic_name__regex=r'S')
    # data = topic.objects.filter(topic_name__contains='e').order_by(Length('topic_name'))
    # data = topic.objects.filter(topic_name__contains='e').order_by(Length('topic_name').desc())
    # data = topic.objects.exclude(topic_name__contains='e')
    # data = access.objects.filter(date__week=15)#we've to add week of the year from 1-52or 53
    # data = access.objects.filter(date__week_day=2)#week starts from sunday(1) to saturday(7)
    
    # data = access.objects.filter(date__week=15) or (author__contains='e')#here it'll return error cause both of the condtions return queryset so it is difficult to concatinate those
    # data = access.objects.filter(Q(date__week=25) & Q(author__contains='A'))
    # data = access.objects.filter(date__week=15,author__contains='e')#work for and condition it's shortcut for baove condition
    # data = access.objects.filter(Q(date__week=25) | Q(author__regex='A'))#we can use Qonly dealing with orWe cxan't use shortcut 
    # data=webpage.objects.prefetch_related('access_set').all()
    data=dept.objects.prefetch_related('emp_set').all()




    return render(re,'all.html',{'columns':columns,'data':data})

