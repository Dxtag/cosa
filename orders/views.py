from django.shortcuts import render, redirect ,get_object_or_404
from .models import Order, OrderProduct
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib import messages


# ---- list views ----
@staff_member_required
def staff_orders_view(request):
    orders = Order.objects.filter(
        is_paid=True, is_sent=False).order_by("-order_date")
    return render(request, "orders/orders.html", {"orders":orders})

@login_required
def orders_view(request):
    return render(request, "orders/orders.html", {"orders":request.user.orders.all()})


# ---- detail views ----
@staff_member_required
def staff__detail_order_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    products = order.products.all()
    return render(request, "orders/order_detail.html", {"order":order, "products":products})

@login_required
def detail_order_view(request, pk):
    order = get_object_or_404(request.user.orders.all(), pk=pk)
    products = order.products.all()
    return render(request, "orders/order_detail.html", {"order":order, "products":products})



@login_required
def place_order(request, inpost):
    basket_products = request.user.basket.products.all()
    order = Order(customer=request.user, inpost_code=inpost)
    order.save()
    
    for product in basket_products:
        product.product.stock -= product.quantity
        product.product.save()
        order_product = OrderProduct(quantity=product.quantity, product=product.product, price=product.product.price, order=order)
        order_product.save()

    basket_products.delete()
    messages.success(request, "Zamówienie utworzono")
    return redirect("orders:orders")



