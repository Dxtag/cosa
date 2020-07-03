from django.test import TestCase
from .models import Comment
from shop.models import Product
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your tests here.
class CommentAddTest(TestCase):
    def setUp(self):
        self.u = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass'
        )
        self.p = Product(name="p", description="p", price=1, stock=1)
        self.p.save()
        self.client.login(username="testuser", password="testpass")
    
    def test_add_comment_view(self):
        self.client.post(reverse("comments:add_comment"), {"content":"test", "stars":3, "pk":1})
        self.assertEqual(self.u.comments.count(),1)
        self.assertEqual(self.p.comments.count(),1)