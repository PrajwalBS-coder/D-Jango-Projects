from django.db import models

# Create your models here.
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
class country(models.Model):
    country_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self) -> str:
        return self.country_name

class capital(models.Model):
    country_name=models.OneToOneField(country,on_delete=models.CASCADE,default=" ")
    capital_name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.capital_name
    
class dept(models.Model):
    dno=models.PositiveIntegerField(auto_created=True)
    dna=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return str(self.dno)
class emp(models.Model):
    eno=models.IntegerField()
    dno=models.ForeignKey(dept,on_delete=models.CASCADE,default=1)
    ename=models.CharField(max_length=100)
    def __str__(self):
        return self.ename

