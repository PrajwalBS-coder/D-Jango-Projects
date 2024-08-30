from django.shortcuts import render

# Create your views here.
app_name='movie'
def movie(re):
    return render(re,'movie.html')
