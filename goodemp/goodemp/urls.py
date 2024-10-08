"""
URL configuration for goodemp project.

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
    path('result/',op,name='op'),
    path('insert/',insert,name='insert'),
    path('insert2/',insert2,name='insert2'),
    path('disp/',disp,name='disp'),
    path('empmgr/',empmgr,name='empmgr'),
    path('empmgrdept/',empmgrdept,name='empmgrdept'),
]
