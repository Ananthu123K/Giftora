from django.db import models

# Create your models here.

class CategoryDb(models.Model):
    Category_name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    Cover_Image=models.ImageField(upload_to='category_image', null=True, blank=True)

class GiftDb(models.Model):
    Gift_name = models.CharField(max_length=100,null=True,blank=True)
    Category = models.CharField(max_length=100,null=True,blank=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    Stock = models.PositiveIntegerField(default=0,null=True,blank=True)
    Brand = models.CharField(max_length=100, blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Gift_image = models.ImageField(upload_to="gift_images", blank=True, null=True)
    Created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.Gift_name



