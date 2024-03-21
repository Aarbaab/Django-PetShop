from django import template
from datetime import datetime as t

register=template.Library()

def printd(value):
    return t.now().strftime("%d-%m-%Y %H:%M:%S")

register.filter("PrintDate",printd)
@register.filter(name="multiply")
def Multiply(v1,v2):
    return v1*v2

