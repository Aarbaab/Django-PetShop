from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registerform(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","first_name","last_name"]
        labels={"username":"User","email":"Enter Email","first_name":"Enter First Name","last_name":"Enter Last Name"}
        #Above labels dictionary is used to change the label names of the fields
        #fields="__all__" This gives all the fields i.e Variables availabe in the User model of the user 