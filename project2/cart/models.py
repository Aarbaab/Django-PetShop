from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from product.models import Product 

# Create your models here.
class Cart(models.Model):
    user=models.OneToOneField(User,  on_delete=models.CASCADE)
    products=models.ManyToManyField(Product,through="CartItem")

class CartItem(models.Model):
    cart_id=models.ForeignKey(Cart,on_delete=models.CASCADE)
    pro_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    Quantity=models.PositiveIntegerField(default=1)

class Order(models.Model):
    order_id=models.CharField(max_length=200,primary_key=True,default="Orderxyz")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=300)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()
    phoneno=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.First_Name}-{self.created_at}"




class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    total=models.IntegerField()
    



