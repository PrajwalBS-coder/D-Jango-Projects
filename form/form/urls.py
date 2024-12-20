"""
URL configuration for form project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('naform/',get_name,name='naform'),
    path('thank/',thank,name='thank'),
    path('Patients_details/',Patients_details,name='Patients_details'),
    path('topic_insert/',topic_insert,name='topic_insert'),
    path('webpage_insert/',webpage_insert,name='webpage_insert'),
    path('access_insert/',access_insert,name='access_insert'),
    path('multiple_topic_data/',multiple_topic_data,name='multiple_topic_data'),
    path('multiple_webpage_data/',multiple_webpage_data,name='multiple_webpage_data')
]
