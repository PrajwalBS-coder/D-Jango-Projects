from django.db import models
from django.core.validators import *
# Create your models here.
class AllinOne(models.Model):
    Name=models.CharField(max_length=100,validators=[MinLengthValidator(5)])
    email=models.EmailField(validators=[EmailValidator('Invalid Email')])
    url=models.URLField(validators=[URLValidator])
    text=models.CharField(max_length=100,validators=[EmailValidator(),MaxLengthValidator(19)],default=None)
    age=models.CharField(max_length=100,validators=[MinValueValidator(18),integer_validator()])
    age2=models.CharField(max_length=100,validators=[MaxValueValidator(50),DecimalValidator()])


    def __str__(self):
        return (self.email)

class StudentData(models.Model):
    name=models.CharField(max_length=100)
    sid=models.IntegerField()
    email=models.EmailField()
    url=models.URLField()
    address=models.TextField()
    password=models.CharField(max_length=100)
    def __str__(self):
        return (self.name)