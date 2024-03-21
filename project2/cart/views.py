from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from product.models import Product
from .models import Cart,CartItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def add_to_cart(request,productid):
    #Logic for adding in cart
    product=get_object_or_404(Product,id=productid)
    #print(product.Pro_brand,product.Pro_price,product.Pro_name)
    #Fetching current User
    currentUser=request.user
    cart,created=Cart.objects.get_or_create(user=currentUser)
    #print(cart,created)
    item,item_created=CartItem.objects.get_or_create(cart_id=cart,pro_id=product)
    #print(item,item_created)
    quantity=request.GET.get("quantity")
    item.Quantity=int(quantity)

    if not item_created:
        item.Quantity+=quantity
    
    item.save()
    return HttpResponseRedirect("/product/products/")

#Viewing The cart
@login_required(login_url="/login/")
def viewCart(request):
    currentuser=request.user
    cart,created=Cart.objects.get_or_create(user=currentuser)
    Cartitems=cart.cartitem_set.all()
    FinalAmount=0
    for i in Cartitems:
        FinalAmount+=i.Quantity*i.pro_id.Pro_price
    #print(Cartitems)
    return render(request,"cart.html",{"items":Cartitems,"finalamount":FinalAmount})
def UpdateCart(request,cartItemId):
    cart_item=get_object_or_404(CartItem,pk=cartItemId)
    quantity=request.GET.get("quantity")
    quantity=int(quantity)
    cart_item.Quantity=quantity
    cart_item.save()
    return HttpResponseRedirect("/cart/")

def Delete_Cart(request,cartItemId):
    cart_item=get_object_or_404(CartItem,pk=cartItemId)
    cart_item.delete()
    
    return HttpResponseRedirect("/cart/")



from .forms import OrderForm
from .models import Order,OrderItem
import uuid
def Checkout(request):
    currentUser = request.user
    initial = {
         "user":currentUser ,
         "First_Name":currentUser.get_short_name(),
         "Last_Name":currentUser.last_name
    }
    print(initial['user'])
    print(initial['First_Name'])
    print(initial['Last_Name'])
    form = OrderForm(initial = initial )

    currentUser = request.user
    cart,created = Cart.objects.get_or_create(user=currentUser)
    cartItems = cart.cartitem_set.all()
    print(cartItems)
    finalAmount = 0

    for item in cartItems:
        finalAmount += item.Quantity*item.pro_id.Pro_price
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            #user=form.cleaned_data['user'] as we have excluded the user from form to remove user we will use now
            user=request.user
            firstname=form.cleaned_data['First_Name']
            lastname=form.cleaned_data['Last_Name']
            address=form.cleaned_data['Address']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            pincode=form.cleaned_data['pincode']
            phoneno=form.cleaned_data['phoneno']
            orderId=str(uuid.uuid4())


            order=Order.objects.create(user=user,First_Name=firstname,Last_Name=lastname,
                                 Address=address,city=city,state=state,pincode=pincode,phoneno=phoneno,order_id=orderId[:8])
            for item in cartItems:
                OrderItem.objects.create(
                    order=order,
                    products=item.pro_id,
                    quantity=item.Quantity,
                    total=item.Quantity*item.pro_id.Pro_price
                )



        return HttpResponseRedirect("/payment/"+orderId[:8])
        
    
    return render(request,"checkout.html", {"form":form,"items":cartItems,"finalAmount":finalAmount})


import razorpay
def MakePayment(request,orderId):
    #print(orderId)
    orders=Order.objects.get(pk=orderId)
    orderitems=orders.orderitem_set.all()
    amount=0
    for item in orderitems:
        amount+=item.total
    print(amount)

    client = razorpay.Client(auth=("rzp_test_r4Gw8gNQHYn21G", "mCHiopdAM4JFzmgnAQYQdd7s"))

    data = { "amount": amount*100, "currency": "INR", "receipt": orderId ,"payment_capture":1}
    payment = client.order.create(data=data)
    return render(request,'payment.html',{'payment':payment})




from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.template.loader import render_to_string


@csrf_exempt
def suc(request,orderId):
    if request.method=="POST":
        client = razorpay.Client(auth=("rzp_test_r4Gw8gNQHYn21G", "mCHiopdAM4JFzmgnAQYQdd7s"))
        check=client.utility.verify_payment_signature({
            'razorpay_order_id': request.POST.get("razorpay_order_id"),
            'razorpay_payment_id': request.POST.get("razorpay_payment_id"),
            'razorpay_signature': request.POST.get("razorpay_signature") 
            })
        if check:
            orders=Order.objects.get(pk=orderId)
            orders.paid=True
            orders.save()
            user=request.user
            orderItems=orders.orderitem_set.all()
            send_mail(
                "Order Placed..",
                "",
                "sharmuankit@gmail.com",
                ["jari.jafri21@gmail.com","priyanka.vibhute@itvedant.com","roushanshaikh040403@gmail.com"],
                fail_silently=False,
                html_message=render_to_string("email2.html",{"items":orderItems,"user":user})
            )
            cart=Cart.objects.get(user=request.user)
            cart.delete()
        
            return render(request,"success.html",{})



        
    
