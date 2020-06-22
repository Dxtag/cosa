from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from .models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class index_view(ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name = "products"


class product_view(DetailView):
    model = Product
    template_name = "shop/product.html"
    context_object_name = "product"

def basket_view(request):
    #testowo
    return render(request, "shop/basket.html", {"products":Product.objects.all()})




    
