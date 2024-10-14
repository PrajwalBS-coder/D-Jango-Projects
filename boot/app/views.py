from django.shortcuts import render

# Create your views here.
def boot(re):
    return render(re, 'boots.html')