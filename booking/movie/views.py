from django.shortcuts import render

# Create your views here.
def movie(re):
    return render(re,'movie.html')
