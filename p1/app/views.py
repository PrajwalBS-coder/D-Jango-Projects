from django.shortcuts import render
from django.http import HttpResponse as hr
from time import gmtime, strftime
import time
# Create your views here.
def wish(request):
    s = strftime("%a, %d %b %Y %H:%M:%S", 
             gmtime(time.time()))
    obj = time.strptime(s, "%a, %d %b %Y %H:%M:%S")
    if(obj.tm_hour+5)<12:
        return hr("Good Morning")
    elif(obj.tm_hour+5)<18:
        return hr("Good Afternoon")
    else:
        return hr("Good Evening")