from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField
from datetime import datetime, timedelta
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    price = models.DecimalField(max_digits=6, decimal_places=2)

    photo = models.ImageField(upload_to="shop/product", default="shop/product/default.png")

    pub_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)

    purchases = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField()

    is_archival = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def is_new(self):
        return True if (timezone.now() - self.pub_date) < timedelta(days=7) and timezone.now() >= self.pub_date else False

    def is_future(self):
        return True if timezone.now() <= self.pub_date else False


class Basket(models.Model):
    customer = AutoOneToOneField(
        User, on_delete=models.CASCADE, related_name="basket")

    def __str__(self):
        return f"{self.customer} basket"

    def basket_price(self):
        price = [i.full_price() for i in self.products.all()]
        return sum(price)

class BasketProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )

    basket = models.ForeignKey(
        Basket, on_delete=models.CASCADE, related_name="products")

    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} in {self.basket.customer} basket"

    def full_price(self):
        return self.product.price * self.quantity
