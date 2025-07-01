from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    contact=models.IntegerField()
    password=models.CharField(max_length=10)
    confirmpassword=models.CharField(max_length=10)
    DOB=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    education=models.CharField(max_length=20)
    profile=models.ImageField(upload_to="images/")
    resume=models.FileField(upload_to="files/")
    

class Login(models.Model):
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    
class Query(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    query=models.TextField(max_length=50)
    

    
    
    
    
    