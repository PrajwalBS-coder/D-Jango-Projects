from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView as t
from django.views import View as v
from django.http import HttpResponse as hr
class One(t):
    template_name="one.html"

class greet(v):
    statement='Class Based Views'
    def get(s,re):
        return hr(f"<center><h1> {s.statement} </h1></center>")