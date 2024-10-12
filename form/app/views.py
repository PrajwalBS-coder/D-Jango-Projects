from django.shortcuts import render
from .models import *
from django.db.models import *

# Create your views here.
def Insert_Product_cat(re):
    pcid=input("ENter ProductId")
    pcname=input("ENter ProductCategories Name")
    source=input("Enter The Source")
    ProductCategoryies.objects.create(pcid=pcid,product_category_name=pcname,source=source)
    columns=[field.name for field in ProductCategoryies._meta.get_fields()]
    PCO= ProductCategoryies.objects.all()
    return render(re,'all.html',{'data':PCO,'columns':columns})
def Display_Product_cat(re):
    columns=[field.name for field in ProductCategoryies._meta.get_fields()]
    PCO= ProductCategoryies.objects.all()
    return render(re,'all.html',{'data':PCO,'columns':columns})

def Insert_Product(re):
    pid=input("ENter ProductId")
    pcid=input("ENter PProductCategories Id")
    pname=input("ENter ProductCategories Name")
    price=input("Enter The Source")
    manu=input("enter Manufacture")
    date=input("Enter date")
    PCOBJ=ProductCategoryies.objects.filter(pcid=pcid)
    if (PCOBJ):
        Product.objects.create(pid=pid,pcid=PCOBJ[0],pname=pname,price=price,manufacture=manu,mdate=date)
        columns=[field.name for field in Product._meta.get_fields()]
        PCO= Product.objects.all()
        return render(re,'all.html',{'data':PCO,'columns':columns})
def Display_Product(re):
    columns=[field.name for field in Product._meta.get_fields()]
    PCO= Product.objects.all()
    return render(re,'all.html',{'data':PCO,'columns':columns})
def Queries(re):
    columns1=[field.name for field in Product._meta.get_fields()]
    columns2=[field.name for field in ProductCategoryies._meta.get_fields()][1::]
    columns=columns1+columns2
    PCO= ProductCategoryies.objects.prefetch_related('product_set')
    p= Product.objects.all().aggregate(Avg('price'))
    p= Product.objects.all().aggregate(Min('price'))
    p= Product.objects.all().aggregate(Max('price'))
    p= Product.objects.all().aggregate(Count('price'))
    p= Product.objects.all().aggregate(Sum('price'))
    print(p)
    return render(re,'all.html',{'data':PCO,'columns':columns})