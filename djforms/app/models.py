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
    
class stud(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.name