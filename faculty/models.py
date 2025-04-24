from django.db import models

# Create your models here.
class faculty(models.Model):
    name=models.CharField(max_length=50,default=None)
    badge=models.CharField(max_length=10,default=None)
    title=models.CharField(max_length=50,default=None)
    img=models.ImageField()
    description=models.CharField(max_length=150,default=None)
    dept=models.CharField(max_length=30,default=None)
    courses=models.IntegerField(max_length=2,default=None)
    rating=models.IntegerField(max_length=2,default=None)
    paper=models.IntegerField(max_length=3,default=None)
    
