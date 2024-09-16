from django.shortcuts import render

# Create your views here.
def online(re):
    return(render(re,'mdb.html'))
def download(re):
    return render(re,'download.html')