from django.db import models

# Create your models here.

class cartdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Total = models.IntegerField(null=True,blank=True)

class customerdb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Confirmpassword = models.CharField(max_length=100, null=True, blank=True)
