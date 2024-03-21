from django.db import models



class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('Pro_name')
class ProductPri(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('Pro_price') 


class pri(models.Manager):
    def get_queryset(self):
        #return super().get_queryset().filter(Pro_price__gte=500)
        #return productQuerySet(self.model).getPawsIndia()
        return productQuerySet(self.model)
    def sorted(self):
        return super().get_queryset().order_by('Pro_name')
    
    def sortbyprice(self):
        return super().get_queryset().order_by('Pro_price')

class productQuerySet(models.QuerySet):
    def getPawsIndia(self):
        return self.filter(Pro_name="Brush")
    def sortbychar(self):
        return self.filter(Pro_name__icontains="c")
    def sortbyp(self):
        return self.filter(Pro_name__iendswith='S')

