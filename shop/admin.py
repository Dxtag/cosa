from django.contrib import admin
from .models import Product, Order, BasketProduct, Basket
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Basket)
admin.site.register(BasketProduct)


