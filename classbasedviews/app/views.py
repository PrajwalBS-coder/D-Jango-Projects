from django.shortcuts import render
from django.views.generic import *
from .forms import *
# Create your views here.
from django.http import *
def Fun(re):
    return HttpResponse("Function")


class Fun2(View):
    def get(self,re):
        return HttpResponse('ClassBased')
    

class Form(View):
    def get(self,re):
        return render(re,'Form.html',{'obj':Sform()})
    
    def post(self,re):
        data=Sform(re.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('OK')
        else:
            HttpResponse("Gone")
