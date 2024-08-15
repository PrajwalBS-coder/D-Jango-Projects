from django.shortcuts import render
from django.http import HttpResponse as hr
from time import gmtime, strftime
# Create your views here.
def wish(request):
    s = strftime("%a, %d %b %Y %H:%M:%S", 
             gmtime(1627987508.6496193))
    
    return hr("Evening")