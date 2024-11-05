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
            sclm=[clm.name for clm in StudentData._meta.get_fields()]
            s=StudentData.objects.get_or_create(name=re.POST.get('sname'),
            sid=re.POST.get('id'),
            email=re.POST.get('email'),
            url=re.POST.get('url'),
            address=re.POST.get('address'),
            password=re.POST.get('password'))
            sobj=StudentData.objects.filter(name=re.POST.get('sname'))
            if(s):
                # return hr(str(SDATA.cleaned_data))
                return render(re,'disp.html',{'clm':sclm,'data':sobj})
            else:
                hr("NOT ADDED TO DB")
            # print(re.POST.get('password'))
            # return hr(SDATA)
        else:
            return hr("WRONG")
    return render(re,'form.html',{'form':s})


def insertTopic(re):
    if(re.method=='POST'):
        data=TopicForm(re.POST)
        if(data.is_valid()):
            topic.objects.get_or_create(topic_name=re.POST['tn'])
    return render(re,'insertTopic.html',{'form':TopicForm()})
def insertwebpage(request):
    if(request.method=='POST'):
        data=webpageForm(request.POST)
        if data.is_valid():
            po=topic.objects.get(topic_name=request.POST['tn'])
            wo=webpage.objects.get_or_create(topic_name=po,name=request.POST['nm'],url=request.POST['url'],email=request.POST['email'])
            if wo:
                return hr("DONE")
            else:
                return hr('NOIDEA')
    return render(request,'insertwebpage.html',{'form':webpageForm()})

def insertaccess(request):
    if(request.method=='POST'):
        data=AccessForm(request.POST)
        if data.is_valid():
            po=webpage.objects.get(id=request.POST['name'])#here request.POST['name'] return primary key value so id is taken
            wo=access.objects.get_or_create(name=po,author=request.POST['author'],date=request.POST['date'])
            if wo:
                return hr("DONE")
            else:
                return hr('NOIDEA')
    return render(request,'insertwebpage.html',{'form':AccessForm()})


def insertstu(request):
    if(request.method=='POST'):
        data=student(request.POST)
        if data.is_valid():
            so=stud.objects.get_or_create(id=request.POST['id'],name=request.POST['name'],email=request.POST['email'])
            if so:
                return hr("DONE")
            else:
                return hr('NOIDEA')
        else:
            hr('GONE')


    return render(request,'insertTopic.html',{'form':student()})
