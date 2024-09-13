from django.shortcuts import render

# Create your views here.
def down(re):
    return render(re,'download.html')
def online(re):
    return render(re,'cdn.html')