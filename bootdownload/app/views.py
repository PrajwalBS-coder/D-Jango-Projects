from django.shortcuts import render

# Create your views here.
def down(re):
    return render(re,'download.html')
def online(re):
    return render(re,'cdn.html')
def dummy(re):
    return render(re,'dummy.html')
def car(re):
    return render(re,'car.html')
def card(re):
    return render(re,'card.html')

def alert(re):
    return render(re,'alert.html')
def badge(re):
    return render(re,'badge.html')
