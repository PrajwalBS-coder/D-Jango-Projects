from django.shortcuts import render

# Create your views here.
app_name='cab'
def cab(re):
    return render(re,'cab.html')