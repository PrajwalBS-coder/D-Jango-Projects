from django.shortcuts import render
from django.http import HttpResponse as hr
# Create your views here.
def send(re):
    return hr('1000 Rs Send To !@#$')
def recive(re):
    return render(re,'receive.html')