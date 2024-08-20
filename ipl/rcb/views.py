from django.shortcuts import render
from django.http import HttpResponse as hr

def virat(re):
    return hr('<h1>Virat Is The Best Second Down Bater</h1>')
def abd(re):
    return render(re,'abd.html')