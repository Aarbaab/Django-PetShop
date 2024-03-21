
import imp
from django.shortcuts import render
from django.views.generic.list import ListView 
from . import models as m
from django.views.generic import DetailView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class ProductView(ListView):
    model=m.Product
    template_name="products.html"
@method_decorator(login_required(login_url="/login/"),name="dispatch")
class ProdetView(DetailView):
    model=m.Product
    template_name="products_detail.html"
    context_object_name="p"

def field_lookup(request):
    #products=m.Product.pm.all().filter(Q(id=9)&Q(Pro_name="Brush"))
    #products=m.Product.pm.all().filter(Q(Pro_price__lt=5000)&Q(Pro_name__icontains="s"))
    #products=m.Product.pm.all().filter(Q(id=5)|Q(id=7))
    products=m.Product.pm.all().filter(~Q(Pro_brand="Paws"))

    #products=m.Product.objects.all() we have changed our manager name in model file to pm object is default manager name
    #products=m.Product.pm.all()
    #products=m.Product.cm.all()our first custom manager
    #products=m.Product.pr.all()
    #products=m.Product.price_500.all()
    #products=m.Product.price_500.sorted()#Custom method function made by us .all is default
    #products=m.Product.price_500.all().getPawsIndia()
    #products=m.Product.price_500.sortbyprice()
    #products=m.Product.price_500.all().sortbychar()
    #products=m.Product.price_500.all().sortbyp()
    #products=m.Product.objects.filter(Pro_name="Brush")
    #products=m.Product.objects.filter(Pro_price__gte=500)#Double uderscore and lt means lte means less than and equal to similarly gt and gte
    #products=m.Product.objects.filter(Pro_name__contains="C")#contains work like 'like'keyword in sql it is case sensitive
    #products=m.Product.objects.filter(Pro_name__icontains="c")#same as contains diff is this is not case sesitive
    #products=m.Product.objects.filter(Pro_name__startswith="C")#case sesnsitive
    #products=m.Product.objects.filter(Pro_name__istartswith="c")#case insesnsitive
    #products=m.Product.objects.filter(Pro_name__endswith="s")#case sesnsitive
    #products=m.Product.objects.filter(Pro_name__iendswith="S")
    #products=m.Product.objects.filter(id__in=[5,6])
    return render(request,'productlook.html',{"product":products})

class categoryDetailView(DetailView):
    model=m.Category
    template_name="category.html"
    context_object_name="category"
    slug_field="slug"
