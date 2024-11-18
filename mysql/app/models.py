from django.db import models

# Create your models here.
class Profile(models.Model):
    user_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    def __str__(s):
        return s.address
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    def __str__(s):
        return s.name
