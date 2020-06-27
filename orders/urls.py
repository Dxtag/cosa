from django.urls import path
from .views import staff_orders_view, orders_view, place_order, staff__detail_order_view, detail_order_view

app_name = "orders"

urlpatterns = [
    path("", orders_view, name="orders"),
    path("staff", staff_orders_view, name="staff_orders"),
    path("make_order/<str:inpost>", place_order, name="place_order"),
    path("staff/<int:pk>", staff__detail_order_view, name="staff_orders_detail"),
    path("<int:pk>", detail_order_view, name="order_detail"),
    
]
