from django.shortcuts import render
from .models import *
from django.db.models import *
from django.http import HttpResponse as hr
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
    price=input("Enter The Price")
    manu=input("enter Manufacture")
    date=input("Enter date")
    PCOBJ=ProductCategoryies.objects.filter(pcid=pcid)
    if (PCOBJ):
        if(pid and pcid and pname and price and manu and date):
            Product.objects.create(pid=pid,pcid=PCOBJ[0],pname=pname,price=price,manufacture=manu,mdate=date)
            columns=[field.name for field in Product._meta.get_fields()]
            PCO= Product.objects.all()
            return render(re,'all.html',{'data':PCO,'columns':columns})
        else:
            return hr('Not A Valid Data')
    else:
        return hr('Product Catgories Does NOt Exist')
def Display_Product(re):
    columns=[field.name for field in Product._meta.get_fields()]
    PCO= Product.objects.all()
    return render(re,'all.html',{'data':PCO,'columns':columns})
def Queries(re):
    columns1=[field.name for field in Product._meta.get_fields()]
    columns2=[field.name for field in ProductCategoryies._meta.get_fields()][1::]
    columns=columns1+columns2
    PCO= ProductCategoryies.objects.prefetch_related('product_set')
    # PCO= Product.objects.select_related('pcid')
    p= Product.objects.all().aggregate(Avg('price'))
    p= Product.objects.all().aggregate(Min('price'))
    p= Product.objects.all().aggregate(Max('price'))
    p= Product.objects.all().aggregate(Count('price'))
    p= Product.objects.all().aggregate(Sum('price'))
    print(p)
    #updating single row
    Product.objects.filter(pname="Puma").update(price=2545)
    #updating multiple row
    Product.objects.filter(pcid=2).update(price=1522)
    #Zero Rows Nothing Happend
    Product.objects.filter(pcid=4).update(price=1522)
    # Product.objects.filter(price=1522).update(pcid=4)# it'll throw an error cause 4 does not exist

    Product.objects.filter(price=1522).update(pcid=3)
    #update_or_create
    # Product.objects.update_or_create(pname='Puma',defaults={"price":8966})
   
    #update_or_create MultipleObjectsReturned at /Queries/get() returned more than one Product -- it returned 2!
    # Product.objects.update_or _create(pcid=2,defaults={"price":8966})


    # Product.objects.update_or_create(pcid=    ,defaults={"price":8966})
    Product.objects.update_or_create(pname='Puma',defaults={"pcid":ProductCategoryies.objects.get(pcid=3),"price":8966,"mdate":'2022-07-05'})#IntegrityError at /Queries/NOT NULL constraint failed: app_product.mdate
    # Product.objects.update_or_create(pname='Adidas',defaults={"pcid":ProductCategoryies.objects.get(pcid=1),"price":8966,"mdate":'2022-06-05'})#Creating new Row of data 
    # Product.objects.filter(pname='Adidas').delete()
    # Product.objects.filter(manufacture=" ").delete()
    Product.objects.update_or_create(pname='Peter England',defaults={"price":8966,"mdate":'2022-08-05'})
    Product.objects.update_or_create(pname='Peter England',defaults={"price":8966,"mdate":'2022-08-05'})
    return render(re,'all.html',{'data':PCO,'columns':columns})