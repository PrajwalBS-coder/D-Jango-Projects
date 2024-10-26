from django.db import models

# Create your models here.
class StudentData(models.Model):
    name=models.CharField(max_length=100)
    sid=models.IntegerField()
    email=models.EmailField()
    url=models.URLField()
    address=models.TextField()
    password=models.CharField(max_length=100)
    def __str__(self):
        return (self.name)