from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def getfilename(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename ="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Catagory(models.Model):
    name=models.CharField(max_length=100, null=False, blank=False)
    image=models.ImageField(upload_to=getfilename, null=True, blank=True)
    description=models.TextField(max_length=500, null=False, blank=False)
    status=models.BooleanField(default=False, help_text="0-default, 1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    catagory=models.ForeignKey(Catagory, on_delete=models.CASCADE)
    name=models.CharField(max_length=100, null=False, blank=False)
    vendor=models.CharField(max_length=150, null=False, blank=False)
    quantity=models.IntegerField(null=False, blank=False)
    old_price=models.FloatField(null=False, blank=False)
    new_price=models.FloatField(null=False, blank=False)
    image=models.ImageField(upload_to=getfilename, null=True, blank=True)
    description=models.TextField(max_length=500, null=False, blank=False)
    status=models.BooleanField(default=False, help_text="0-default, 1-hidden")
    trending=models.BooleanField(default=False, help_text="0-default, 1-trending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    products=models.ForeignKey(Products, on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False, blank="False")
    created_at=models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.product_qty * self.products.new_price
    

class Favourite(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    products=models.ForeignKey(Products, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
