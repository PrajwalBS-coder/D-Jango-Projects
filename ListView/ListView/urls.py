"""
URL configuration for ListView project.

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
from django.urls import path,re_path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/',SchholList.as_view(),name='school'),
    path('stu/',StudentList.as_view(),name='stu'),
    path('CreateSchool/',CreateSchool.as_view(),name='CreateSchool'),
    # path('school/<pk>/',SchoolDetails.as_view(),name='details'),
    # path('school/update/<pk>/',UpdateSchool.as_view(),name='updateSchool'),#working fine
    
    # re_path('(?P<pk>\d+)/update$/',UpdateSchool.as_view(),name='updateSchool'),
    re_path(r'^(?P<pk>\d+)/update/$', UpdateSchool.as_view(), name='updateSchool'),#updateview should come first before detail view while using re_path()
    re_path(r'^(?P<pk>\d+)/delete/$', DeletVSchool.as_view(), name='deleteSchool'),
    re_path('(?P<pk>\d+)/',SchoolDetails.as_view(),name='details'),

]