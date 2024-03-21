from django.shortcuts import render,HttpResponse
from django.views import View

# Create your views here.
def home(request):
    return HttpResponse("WEB URL First view")
def about(request):
    return HttpResponse("THis is about us")
def FirstPage(request):
    return HttpResponse("<h1>This is first page</h1>")
def Users(request):
    school={
        "id":101,
        "Name":"FHS",
        "Students":1500
    }
    return render(request,"index.html",school)
def Login(request):
    student={
        "id":101,
        "Name":"Nikki",
        "age":18
    }
    return render(request,'login.html',student)#Here we have passed the dictionary we will use the values of dictionary in login.html using key name
#To access in html file we use {{KEY_NAME}} this will return the value associated with our key name in our html page
def form(request):
    return render(request,"form.html")
def submit(request):
    if request.method=="POST":
      return render(request,"submit.html")
    if request.method=="GET":
        return render(request,"form.html")
    
#Class based view
class firstView(View):
    def get(self,request):
        return HttpResponse("Class based view GETTT method")
    
class SecondView(View):
    name="Nikki"
    def get(self,request):
        return render(request,"detail.html",{"name":self.name})


