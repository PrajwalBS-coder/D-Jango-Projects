from django.urls import path
from India.views import *

urlpatterns=[
    path('captain/',captain,name='captain')
]