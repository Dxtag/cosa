from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class index_view(ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name = "products"

class product_view(DetailView):
    model = Product
    template_name = "shop/product.html"
    context_object_name = "product"