from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.auth.models import User
from django.views.generic import ListView

#Wszystkie strony związane z koszykiem 
from .views_basket import add_to_basket, set_quantity, basket_view


class index_view(ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name = "products"

    def get_queryset(self):
        return self.model.objects.filter(is_archival=False)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        quantity = request.POST["quantity"]
        return redirect("shop:add_to_basket", pk, quantity)

    return render(request, "shop/product.html", {"product": product})


