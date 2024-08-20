from django.shortcuts import render

from django.http import HttpResponse as hr

def recharge(re):
    return hr('<h1>1000 Rs Recharged To Airtel </h1>')
def update(re):
    return render(re,'update.html')
