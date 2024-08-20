from django.shortcuts import render
from django.http import HttpResponse as hr

def rohit(re):
    return hr('<h1>Rohit Is The Best Openning Batsman</h1>')
def pandya(re):
    return render(re,'pandya.html')
# Create your views here.
