from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.auth.models import User
from django.views.generic import ListView
from comments.forms import CommentForm

#Wszystkie strony związane z koszykiem 
from .views_basket import add_to_basket, basket_view


class IndexView(ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name = "products"

    def get_queryset(self):
        return self.model.objects.filter(is_archival=False)


def product_view(request, pk):
    if request.method == "POST":
        quantity = request.POST["quantity"]
        return redirect("shop:add_to_basket", pk, quantity)
    form = CommentForm
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all()
    return render(request, "shop/product.html", {"product": product, "form":form, "comments":comments} )


