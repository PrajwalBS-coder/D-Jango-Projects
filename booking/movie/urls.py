from django.urls import path
from movie.views import *

urlpatterns=[
    path('movie/',movie,name='movie'),
]