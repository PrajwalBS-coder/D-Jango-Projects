from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=100)
    blood_group=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    health_tips=models.TextField(max_length=150)