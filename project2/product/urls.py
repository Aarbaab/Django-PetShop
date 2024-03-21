from django.contrib import admin
from django.urls import path,include
from .views import ProdetView,ProductView,field_lookup,categoryDetailView


urlpatterns = [
    path('products/',ProductView.as_view(),name="products"),
    path('products/<int:pk>',ProdetView.as_view(),name="DetailPro"),
    path('productlookup/',field_lookup),
    path('category/<slug:slug>',categoryDetailView.as_view(),name="category")
]

''' path('admin/', admin.site.urls),
    path('home/',views.home),
    path('about/',views.about,name="About Us"),
    path('',views.FirstPage,name="First Page"),
    path('users/',views.Users,name="Users"),
    path('login/',views.Login,name="Login"),
    path('form/',views.form,name="Form"),
    path('submit/',views.submit,name="submit"),
    path('class/',views.firstView.as_view(),name="class"),
    path('details/',views.SecondView.as_view(name="Danial"),name="details"),'''