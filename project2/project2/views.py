from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from product.models import Product
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import Registerform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def Home(request):
    return render(request,"about.html")

def contact(self,request):
    return render(request,"contact.html")


def home(request):
    username=request.session.get("currentuser",None)
    return render(request,"index.html",{"username":username})

def nav(request):
    username=request.session.get("currentuser",None)
    return render(request,"nav.html",{"username":username})

@login_required(login_url="/login/")
def search(request):
    query=request.GET.get('query','')
    print(query)
    product=Product.pm.all().filter(Pro_name__icontains=query)
    return render(request,'search.html',{"products":product})

def register(request):
    if request.method=="POST":
        #form=UserCreationForm(request.POST)
        form=Registerform(request.POST)
        if form.is_valid():
            form.save()
    else:
        #form=UserCreationForm()
        form=Registerform()
    return render(request,'register.html',{"form":form})
def Login(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            passcode=form.cleaned_data["password"]
            user=authenticate(username=username,password=passcode)
            if user is not None:
                login(request,user)
                request.session["currentuser"]=user.get_username()
                return HttpResponseRedirect("/product/products")#/product/products
    else:
        form=AuthenticationForm()
    return render(request,"login.html",{"form":form})

#User logout Function
def Logout(request):
    logout(request)
    return HttpResponseRedirect("/")
    