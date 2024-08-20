from django.shortcuts import render
from django.http import HttpResponse as hr

def msd(re):
    return hr('<h1>MSD Is The Best</h1>')
def raina(re):
    return render(re,'raina.html')