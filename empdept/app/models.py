from django.db import models

# Create your models here.
class department(models.Model):
    deptno=models.PositiveIntegerField(primary_key=True)
    dna=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.dna
class employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    dno=models.ForeignKey(department,on_delete=models.CASCADE)
    def __str__(self):
        return self.ename
