from django.db import models

# Create your models here.

class admindb(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    EMAIL = models.EmailField(null=True, blank=True)
    NUMBER = models.IntegerField(null=True, blank=True)
    USERNAME = models.CharField(max_length=50, null=True, blank=True)
    PASSWORD = models.CharField(max_length=50, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="profile",null=True, blank=True)

class categordb(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    DISCRIPTION = models.CharField(max_length=100, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="profile",null=True,blank=True)

class productdb(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    CATEGORY = models.CharField(max_length=100, null=True, blank=True)
    PRIZE = models.IntegerField(null=True, blank=True)
    QUANTITY = models.IntegerField(null=True, blank=True)
    DISCRIPTION = models.CharField(max_length=100, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="profile", null=True, blank=True)

class admincontactdb(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    EMAIL = models.EmailField(null=True, blank=True)
    SUBJECT = models.CharField(max_length=50, null=True, blank=True)
    MESSAGE = models.CharField(max_length=100, null=True, blank=True)

class contactdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    LName=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)
