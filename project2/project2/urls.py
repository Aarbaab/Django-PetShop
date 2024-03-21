"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django import views
from django.contrib import admin
from django.urls import path,include
from firstapp import views
from product import views as p
from django.conf.urls.static import static
from project2 import settings
from .views import Home,contact,home,search,register,Login,Logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/',views.SecondView.as_view(name="Danial"),name="details"),
    path('product/',include('product.urls')),
    path('about/',Home,name="Home"),
    path('contact/',contact,name="Contact"),
    path('',home,name="Homeee"),
    path("search/",search,name='search'),
    path("register/",register,name="register"),
    path("login/",Login,name="Login"),
    path("logout/",Logout,name="Logout"),
    path("",include('cart.urls'))
    

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




'''
    path('home/',views.home),
    path('about/',views.about,name="About Us"),
    path('',views.FirstPage,name="First Page"),
    path('users/',views.Users,name="Users"),
    path('login/',views.Login,name="Login"),
    path('form/',views.form,name="Form"),
    path('submit/',views.submit,name="submit"),
    path('class/',views.firstView.as_view(),name="class"),
    path('products/',p.ProductView.as_view(),name="products"),
    path('products/<int:pk>',p.ProdetView.as_view(),name="DetailPro"),
    path('productlookup/',p.field_lookup)

'''