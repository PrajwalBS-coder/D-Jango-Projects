"""
URL configuration for db project.

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
    path('op/',op,name='op'),
    path('insert_topic/',insert_topic,name='insert_topic'),
    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('topic/',topi,name='topic'),
    path('web/',web,name='web'),
    path('empdept/',empdept,name='empdept'),
    path('precap/',precap,name='precap'),
    path('topic_webpage_prefetch/',topic_webpage_prefetch,name='topic_webpage_prefetch'),
    path('webpage_access_prefetch/',webpage_access_prefetch,name='webpage_access_prefetch'),
    path('agg/',agg,name='agg')
    # path('cap/',cap,name='cap'),
    # path('cap2/',cap2,name='cap2')
]
