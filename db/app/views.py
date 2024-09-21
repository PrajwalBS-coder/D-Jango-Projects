from django.shortcuts import render
from app.models import emp

# Create your views here.

def op(re):
    empdet=emp.objects.all()
    print(empdet)
    return render(re,'op.html',{'empdet': empdet})
