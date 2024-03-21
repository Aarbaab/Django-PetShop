from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
#user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Product 
from django.db.models.signals import pre_delete,post_delete,pre_save,post_save 



@receiver(user_logged_in,sender=User)
def log_in(sender,request,user,**kwargs):
    print("sender",sender)
    print("request:",request)
    print("user",user)
    print("Arguments",kwargs)
    print("****************************")
    print("Logged in succesfully")
    print("***************************")

@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("sender",sender)
    print("request:",request)
    print("user",user)
    print("Arguments",kwargs)
    print("****************************")
    print("Logged out succesfully")
    print("***************************")


@receiver(post_save,sender=Product)
def ProductSignal(sender,instance,**kwargs):
    print("*****************Product Created***********************")
    print("************************************************")
    print("sender:",sender)
    print("instance:-",instance)
    print("Arguments:-",kwargs)

@receiver(post_delete,sender=Product)
def Product_del(sender,instance,**kwargs):
    print("**********************Product_Deleted**************************")
    print("***************************************************************")
    print("Sender:-",sender)
    print("Instance:-",instance)
    print("Arguments:-",kwargs)




    
