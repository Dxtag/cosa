from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(verbose_name="Treść")
    class Stars(models.IntegerChoices):
        BARDZO_DOBRY = 5
        DOBRY = 4
        PRZECIĘTNY = 3
        SŁABY = 2  
        BARDZO_SŁABY= 1
    stars = models.IntegerField(choices=Stars.choices, verbose_name="Ocena")
    
    def __str__(self):
        return f"Komentarz {self.user} produktu {self.product}"
    
