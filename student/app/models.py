from django.db import models

# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    def __str__(s):
        return s.name
class student(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    school_name=models.ForeignKey(school,on_delete=models.CASCADE)
    def __str__(s):
        return s.name