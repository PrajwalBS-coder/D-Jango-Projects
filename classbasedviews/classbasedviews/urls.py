"""
URL configuration for classbasedviews project.

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
    path('fun/',Fun,name='Fun'),
    path('fun2/',Fun2.as_view(),name='fun2'),
    path('Form/',Form.as_view(),name='Form'),
    path('RenderHtml/',RenderHtml.as_view(),name='RenderHtml'),
    path('StudentInsert/',StudentInsert.as_view(),name='StudentInsert'),
    path('StudentINsert2/',StudentINsert2.as_view(),name='StudentINsert2')
]
