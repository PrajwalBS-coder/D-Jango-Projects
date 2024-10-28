from django.shortcuts import render
from .forms import *
from django.http import HttpResponse as hr
# Create your views here.


def InsertTopic(re):
    if re.method=='POST':
        dataobj=TopicForm(re.POST)
        if dataobj.is_valid():
            dataobj.save()
            return hr("OK")
        else:
            return hr('Gone')


    return render(re,'insert.html',{'tform':TopicForm()})

def InsertWebpage(re):
    if re.method=='POST':
        dataobj=WebpageForm(re.POST)
        if dataobj.is_valid():
            dataobj.save()
            return hr("OK")
        else:
            return hr('Gone')


    return render(re,'insert.html',{'wform':WebpageForm()})#insertacccess

def InsertAccess(re):
    if re.method=='POST':
        dataobj=AccessForm(re.POST)
        if dataobj.is_valid():
            dataobj.save()
            return hr("OK")
        else:
            return hr('Gone')


    return render(re,'insert.html',{'aform':AccessForm()})#insertacccess
