from django.shortcuts import render

# Create your views here.

def boxmodel(request):
    return render(request,'boxmodel.html')

def dom(request):
    return render(request,'dom.html')

def navbar(request):
    return render(request,'navbar.html')

def table(request):
    return render(request,'tableofmarrige.html')

def signup(request):
    return render(request,'signup.html')