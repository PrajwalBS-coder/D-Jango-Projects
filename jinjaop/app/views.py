from django.shortcuts import render

# Create your views here.
def cond(re):
    return render(re,'cond.html',{'no':10})
