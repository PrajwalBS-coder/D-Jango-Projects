from django.shortcuts import render
from django.http import HttpResponse as hr
from django.http import HttpResponseRedirect as hred
from .forms import * 
# Create your views here.
def get_name(re):
    if re.method=="POST":
        form=Name(re.POST)
        if form.is_valid():
            obj=MyModel.objects.get_or_create(fullname=re.POST['na'],mobile_number=re.POST['number'])
            if obj:
                return hred('/thank/')
            else:
                hr("WrongONe")
            # na=Name.fullname
            # return hr(re.POST['na'])
    else:
        form=Name()
    return render(re,'na.html',{'form':form})

def thank(re):
    return render(re,'thanks.html')

def Patients_details(re):
    if re.method=="POST":
        form=PatientDetails(re.POST)
        if form.is_valid():
            form.save()
            return hred('/thank/')
    else:
        form=PatientDetails()
    return render(re,'na.html',{'form':form})

def topic_insert(re):
    if re.method=='POST':
        tn=re.POST['topic']
        to=topic.objects.get_or_create(topic_name=tn)

        return hred('/thank/') 
    return render(re,'topic_insert.html')
def webpage_insert(re):
    obj=topic.objects.all()
    if re.method=='POST':
        tn=re.POST['tn']
        na=re.POST['name']
        url=re.POST['url']
        em=re.POST['email']
        to=topic.objects.get(topic_name=tn)
        if to:
            print("INSide to")
            wo=webpage.objects.get_or_create(topic_name=to,name=na,url=url,email=em)
            if wo:
                return hred('/thank/') 
            else:
                return hred('/webpage_insert/')  
        else:
            hr("Topic Does't Exist")
    return render(re,'webpage_insert.html',{'to':obj})


def access_insert(re):
    obj=webpage.objects.all()
    if re.method=='POST':
        author=re.POST['author']
        da=re.POST['date']
        wo=webpage.objects.get(id=re.POST['tn'])
        if wo:
            # print("INSide to")
            ao=access.objects.get_or_create(name=wo,author=author,date=da)
            if wo:
                return hred('/thank/') 
            else:
                return hred('/webpage_insert/')
        else:
            hr("Topic Does't Exist")
    return render(re,'access_insert.html',{'wo':obj})
