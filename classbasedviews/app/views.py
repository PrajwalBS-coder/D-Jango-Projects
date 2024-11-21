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



class RenderHtml(TemplateView):
    template_name='fun.html'
    def get_context_data(self, **kwargs):
        EmptyObj= super().get_context_data(**kwargs)
        EmptyObj['name']='Amin'
        return EmptyObj
    


class StudentInsert(TemplateView):
    template_name='fun.html'
    def get_context_data(self, **kwargs):
        EmptyObj= super().get_context_data(**kwargs)
        EmptyObj['form']=Sform()
        return EmptyObj
    
    def post(self,re):
        data=Sform(re.POST)
        if data.is_valid():
            data.save()
            return HttpResponse("OK")
        else:
           return HttpResponse('NOT OK')