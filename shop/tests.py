import datetime
from django.test import TestCase, Client
from .models import BasketProduct, Product, Basket
from django.utils import timezone
from .views import basket_view
from django.shortcuts import reverse
from django.contrib.auth.models import User
from decimal import Decimal, getcontext
# Create your tests here.

class ProductModelTests(TestCase):

    def test_product_is_new_with_future_dates(self):
        future_time=timezone.now()+datetime.timedelta(days=7)
        future_product = Product(pub_date=future_time)
        self.assertIs(future_product.is_new(), False)

    def test_product_is_future_with_old_dates(self):
        old_time=timezone.now() - datetime.timedelta(days=7)
        old_product = Product(pub_date=old_time)
        self.assertIs(old_product.is_future(), False)

class BasketModelTests(TestCase):
    def setUp(self):

        b1 = Product(name="p1", description="p1", price=1, stock=2)
        b2 = Product(name="p2", description="p2", price=1, stock=2)
        b1.save()
        b2.save()
        self.user = User()
        self.user.save()
        self.basket = Basket(customer=self.user)
        self.basket.save()
        p1 = BasketProduct(product=b1, basket=self.user.basket, quantity=2)
        p2 = BasketProduct(product=b2, basket=self.user.basket, quantity=2)
        p1.save()
        p2.save()

    def test_basket_full_price(self):
        price = self.basket.basket_price()
        getcontext().prec = 2
        self.assertEqual(price, Decimal("4.00")) 
        


class BasketViewTest(TestCase):
    def setUp(self):
        self.u = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass'
        )
        self.p = Product(name="p", description="p", price=1, stock=1)
        self.p.save()
        self.client.login(username="testuser", password="testpass")

    def test_adding_too_many_products_to_basket(self):
        c = self.client
        p = self.p
        c.post(reverse("shop:product", kwargs={"pk":p.pk}), data={"quantity":2}, follow=True)
        self.assertEqual(BasketProduct.objects.count(), 0)

    def test_adding_products_to_basket(self):
        c = self.client
        p = self.p
        c.post(reverse("shop:product", kwargs={"pk":p.pk}), data={"quantity":1}, follow=True)
        self.assertEqual(BasketProduct.objects.count(), 1)

    

    
    
