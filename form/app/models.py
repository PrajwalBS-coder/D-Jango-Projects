from django.db import models

# Create your models here.
class ProductCategoryies(models.Model):
    pcid=models.IntegerField(primary_key=True)
    product_category_name=models.CharField(max_length=100)
    source=models.CharField(max_length=100)
    def __str__(self):
        return (self.product_category_name)
class Product(models.Model):
    pid=models.IntegerField(primary_key=True)
    pcid=models.ForeignKey(ProductCategoryies,on_delete=models.CASCADE,null=True)
    pname=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=3)
    manufacture=models.CharField(max_length=100)
    mdate=models.DateField()
    def __str__(self):
        return (self.pname)