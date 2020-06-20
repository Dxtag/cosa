from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to="shop/product")
    add_date = models.DateTimeField(auto_now_add=True)
    purchases = models.IntegerField(default=0)
    stock = models.IntegerField()
    is_archival = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    inpost_code = models.CharField(max_length=6)
    change_date = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(User,on_delete=models.CASCADE, related_name="orders")
    is_paid = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)
    
    def __str__(self):
        if self.is_sent:
            return f"order nr{self.pk} closed"
        elif self.is_paid:
            return f"order nr {self.pk} paid"
        else:
            return f"order nr {self.pk} to pay"
        


class OrderProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="products")
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
