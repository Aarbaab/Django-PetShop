from ast import mod
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from . import managers as m
from autoslug import AutoSlugField


# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=15)
    slug = AutoSlugField(populate_from='title')  #slug=AutoSlugField(populate_from="category_name")

    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    Pro_name=models.CharField(max_length=50,default="productName")
    Pro_desc=models.TextField(default="Write Description")
    Pro_price=models.IntegerField(default=0)
    Pro_brand=models.CharField(max_length=80,default="Paws")
    Pro_image=models.ImageField(upload_to="images/",default="")
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True)
    
    
    
    pm=models.Manager()#changing the manager name to pm default is objects
    cm=m.ProductManager()
    pr=m.ProductPri()
    price_500=m.pri()

    def __str__(self):
        return self.Pro_name
    
    
    '''
            <tr>
            <td>{{p.id}}</td>
            <td>{{p.Pro_name}}</td>
            <td>{{p.Pro_desc}}</td>
            <td>{{p.Pro_price}}</td>
            <td>{{p.Pro_brand}}</td>
        </tr>






         <img src="{{product.Pro_image.url}}" alt="">
        <li>{{product.Pro_name}}</li>
        <li>{{product.Pro_desc}}</li>
        <li>{{product.Pro_price}}</li>
        <li>{{product.Pro_brand}}</li>
    '''
    

