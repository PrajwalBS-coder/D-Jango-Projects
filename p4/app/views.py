from django.shortcuts import render

# Create your views here.
def animation(request):
    return render(request, 'animation.html')
