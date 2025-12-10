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

class CartDb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Giftname=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    TotalPrice=models.IntegerField(null=True,blank=True)
    Gift_Image=models.ImageField(upload_to="CartImages",null=True,blank=True)

class OrderDb(models.Model):
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"