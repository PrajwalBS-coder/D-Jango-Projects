from django.shortcuts import render

# Create your views here.
def jinja(re):
    d={'name':'Jhon'}
    return render(re,'jinja.html',d)