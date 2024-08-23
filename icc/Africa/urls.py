from django.urls import path
from Africa.views import *

urlpatterns=[
    path('captain/',captain,name='captain')
]