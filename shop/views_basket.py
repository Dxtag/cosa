from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Basket, BasketProduct
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def basket_view(request):
    products = request.user.basket.products.all()
    if request.method == "POST":
        return redirect("shop:set_quantity", pk=request.POST["pk"], quantity=request.POST["quantity"])
    return render(request, "shop/basket.html", {"products": products, "basket_price": request.user.basket.basket_price()})


@login_required
def add_to_basket(request, pk, quantity):
    product = get_object_or_404(Product, pk=pk)

    if quantity > product.stock:
        messages.warning(request, f"Nie możesz dodać więcej niż {product.stock} sztuk")
        return redirect("shop:product", pk=pk)

    basket_product, is_created = BasketProduct.objects.get_or_create(
        defaults={"quantity": quantity}, product=product, basket=request.user.basket)
    is_quantity_valid = basket_product.quantity + quantity <= product.stock

    if not is_created and is_quantity_valid:
        basket_product.quantity += quantity
        basket_product.save()

    if quantity == 1:
        messages.success(request, "Dodano 1 sztukę")
    elif 2 <= quantity <= 4:
        messages.success(request, f"Dodano {quantity} sztuki")
    else:
        messages.success(request, f"Dodano {quantity} sztuk")

    return redirect("shop:product", pk=pk)


@login_required
def set_quantity(request, pk, quantity):
    product = get_object_or_404(BasketProduct, pk=pk)

    if quantity == 0:
        product.delete()
    elif quantity <= product.product.stock:
        product.quantity = quantity
        product.save()
    else:
        messages.warning(request, "Nie możesz dodać więcej niż jest na stanie")

    return redirect("shop:basket")
