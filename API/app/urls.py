from django.urls import path
from .views import *



urlpatterns=[
    path('users/',GetUsers,name='GetUser'),
    path('CreateUser/',CreateUser,name='CreateUser')
]