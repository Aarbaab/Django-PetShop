from django.contrib import admin
from . import models as m

# Register your models here.

@admin.register(m.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','Pro_name','Pro_desc','Pro_price','Pro_brand','category')

#admin.site.register(m.Product,ProductAdmin)
@admin.register(m.Category)
class categoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name','slug')
