from django.urls import path
from .views import index_view, product_view, basket_view, add_to_basket, set_quantity, staff_orders_view

app_name = "shop"

urlpatterns = [
    path("", index_view.as_view(), name="index"),
    path("product/<int:pk>", product_view, name="product"),
    path("basket", basket_view, name="basket"),
    path("product/<int:pk>/add:<int:quantity>", add_to_basket, name="add_to_basket"),
    path("basket/<int:pk>/set:<int:quantity>", set_quantity, name="set_quantity"),
    path("staff/orders", staff_orders_view, name="staff_orders")
]
