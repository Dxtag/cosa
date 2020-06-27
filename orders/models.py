from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class Order(models.Model):
    inpost_code = models.CharField(max_length=6)

    change_date = models.DateTimeField(auto_now=True)
    order_date = models.DateTimeField(auto_now_add=True)

    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")

    is_paid = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        if self.is_sent:
            return f"order nr{self.pk} closed"
        elif self.is_paid:
            return f"order nr {self.pk} paid"
        else:
            return f"order nr {self.pk} to pay"
    
    def cost(self):
        cost = sum([i.full_price() for i in self.products.all()])
        return cost


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} in order nr {self.order.pk}"

    def full_price(self):
        return self.price*self.quantity

    
