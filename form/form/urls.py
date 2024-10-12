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
    path('Insert_Product_cat/',Insert_Product_cat,name='Insert_Product_cat'),
    path('Display_Product_cat/',Display_Product_cat,name='Display_Product_cat'),
    path('Insert_Product/',Insert_Product,name='Insert_Product'),
    path('Display_Product/',Display_Product,name='Display_Product'),
    path('Queries/',Queries,name='Queries'),
]
