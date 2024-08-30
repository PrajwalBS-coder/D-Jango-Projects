from django.shortcuts import render

# Create your views here.
def food(re):
    return render(re,'food.html')