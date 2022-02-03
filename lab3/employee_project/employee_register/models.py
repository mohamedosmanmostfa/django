from django.db import models

# Create your models here.


class std(models.Model):
  
    
    std_fname=models.CharField(max_length=10)
    std_lname=models.CharField(max_length=10)
    std_email=models.EmailField(unique=True)
    std_gender=models.CharField(max_length=10)

class myuser(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)    
