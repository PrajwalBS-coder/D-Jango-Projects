from django.db import models
from django.urls import reverse
# Create your models here.
class Ischool(models.Model):
    sname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.sname
    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})

class Student(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    school=models.ForeignKey(Ischool,on_delete=models.CASCADE,related_name='schoolstudent')
    def __str__(self):
        return self.name


