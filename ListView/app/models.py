from django.db import models

# Create your models here.
class Ischool(models.Model):
    sname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.sname

class Student(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    school=models.ForeignKey(Ischool,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


