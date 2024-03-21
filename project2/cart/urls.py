from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path("add-to-cart/<int:productid>",views.add_to_cart,name="addtocart"),
    path("cart/",views.viewCart,name="viewcart"),
    path("cart/update/<int:cartItemId>/",views.UpdateCart,name="UpdateCart"),
    path("cart/delete/<int:cartItemId>",views.Delete_Cart,name="DeleteCart"),
    path("checkout/",views.Checkout,name="Checkout"),
    path("payment/<str:orderId>",views.MakePayment,name="Payment"),
    path("success/<str:orderId>",views.suc,name="success"),     # type: ignore
]
