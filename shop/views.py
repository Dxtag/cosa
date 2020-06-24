from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404 
from django.views.generic import ListView, DetailView
from .models import Product, Basket, BasketProduct, Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User


class index_view(ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name = "products"


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        quantity = request.POST["quantity"]
        return redirect("shop:add_to_basket", pk, quantity)

    return render(request, "shop/product.html", {"product": product})

def staff_orders_view(request):
    orders = Order.objects.filter(is_paid=True, is_sent=False).order_by("order_date")
    if request.method == "POST":
        sent_order = orders.get(pk=request.POST["pk"])
        sent_order.is_sent = True
        sent_order.save()
        return redirect("shop:staff_orders")
    return render(request, "shop/orders.html", {"orders":orders})



@login_required
def basket_view(request):
    products = request.user.basket.products.all()
    if request.method == "POST":
        return redirect("shop:set_quantity", pk=request.POST["pk"], quantity=request.POST["quantity"])
    return render(request, "shop/basket.html", {"products": products})


@login_required
def add_to_basket(request, pk, quantity):

    user_basket = BasketProduct.objects.filter(basket=request.user.basket)
    user_products = user_basket.values_list("product_id", flat=True)
    product = get_object_or_404(Product, pk=pk)

    if product.stock >= quantity:
        if product.pk in user_products:
            basket_product = get_object_or_404(user_basket, product=product)
            if basket_product.quantity + quantity <= product.stock:
                basket_product.quantity += quantity
                basket_product.save()
            else:
                messages.warning(
                    request, "You cannot add more pieces of this product because you have all the pieces in your basket.")
                return redirect("shop:product", pk=pk)
        else:
            basket_product = BasketProduct(
                product=product, basket=request.user.basket, quantity=quantity)
            basket_product.save()

        product.in_basket += quantity
        product.save()
        messages.success(
            request, f"{quantity} x {product.name} added to basket")
        return redirect("shop:product", pk)
    else:
        messages.warning(request, "You cannot add more than is available")
        return redirect("shop:product", pk=pk)


@login_required
def set_quantity(request, pk, quantity):
    product = get_object_or_404(BasketProduct, pk=pk)

    if quantity == 0:
        product.product.in_basket -= product.quantity
        product.delete()
        product.product.save()

    elif product.product.in_basket+product.product.in_basket-quantity <= product.quantity:
        product.product.in_basket -= product.quantity - quantity
        product.quantity = quantity
        product.save()
        product.product.save()
    else:
        messages.warning(request, "You cannot add more than is available")

    return redirect("shop:basket")


@login_required
def place_order():
    pass
