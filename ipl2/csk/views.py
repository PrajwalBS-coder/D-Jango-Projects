from django.shortcuts import render
from django.http import HttpResponse as hr
# Create your views here.
def captain(re):
    return hr("Captain is MSD")
