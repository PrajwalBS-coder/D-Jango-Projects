from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    def __str__(s):
        return s.dname

class Emp(models.Model):
    eno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    hiredate=models.DateField(auto_now=True)
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    dno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    def __str__(s):
        return s.ename