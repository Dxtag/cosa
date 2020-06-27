from django.test import TestCase
from django.test import Client
from django.db import models
from django.contrib.auth.models import User
from shop.models import Product, Basket, BasketProduct
from django.shortcuts import reverse
from .models import Order

class PlaceOrderTest(TestCase):
    def setUp(self):
        self.u = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass'
        )
        self.p = Product(name="p", description="p", price=1, stock=1)
        self.p.save()
        b = Basket(customer=self.u) 
        b.save() 
        BasketProduct(product=self.p, basket=b, quantity=1 ).save()
        self.client.login(username="testuser", password="testpass")
        
    def test_place_order(self):
        self.client.get(reverse("orders:place_order", kwargs={"inpost":"dup123"}), follow=True)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get(pk=1).products.all().count(), 1)
        self.assertEqual(BasketProduct.objects.count(), 0)


