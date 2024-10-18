from django.shortcuts import render
from django.http import HttpResponse as hr
from django.http import HttpResponseRedirect as hred
from .forms import * 
# Create your views here.
def get_name(re):
    if re.method=="POST":
        form=Name(re.POST)
        if form.is_valid():
            # return hr("/OK Done/")
            return hred('/thank/')
            
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
    if re.method=='POST':
        tn=re.POST['topic']
        na=re.POST['name']
        url=re.POST['url']
        em=re.POST['email']
        to=topic.objects.get(topic_name=tn)
        wo=webpage.objects.get_or_create(topic_name=to[0],name=na,url=url,email=em)
        if wo:
            return hred('/thank/') 
        else:
            return hred('/webpage_insert/') 
    return render(re,'webpage_insert.html')