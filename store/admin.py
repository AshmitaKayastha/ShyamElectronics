from django.contrib import admin
from .models import *
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)