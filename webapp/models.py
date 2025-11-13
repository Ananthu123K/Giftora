from django.db import models

# Create your models here.
class RegistrationDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(unique=True, null=True, blank=True)
    Password = models.CharField(max_length=128, null=True, blank=True)
    Confirm_password = models.CharField(max_length=128, null=True, blank=True)

class ContactDb(models.Model):
    User_name=models.CharField(max_length=100,null=True,blank=True)
    User_email=models.EmailField(null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.TextField(null=True,blank=True)
