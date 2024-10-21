from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=100)
    blood_group=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    health_tips=models.TextField(max_length=150)
    def __str__(s):
        return s.name

class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.IntegerField()
    def __str__(s):
        return s.fullname

class topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name

class webpage(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    email=models.EmailField(null=True)
    def __str__(self):
        return self.name

class access(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()
    def __str__(self):
        return self.author