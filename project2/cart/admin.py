from django.contrib import admin
from .models import Order,OrderItem


# Register your models here.
class orderIteminLine(admin.TabularInline):
    model=OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines=[orderIteminLine]


admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
