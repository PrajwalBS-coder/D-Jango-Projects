from django.urls import path
from cab.views import *

urlpatterns=[
    path('cab/',cab,name='cab'),
]