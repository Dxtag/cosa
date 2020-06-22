from django.urls import path
from .views import index_view, product_view, basket_view

app_name = "shop"

urlpatterns = [
    path("", index_view.as_view(), name="index"),
    path("product/<int:pk>", product_view.as_view(), name="product"),
    path("basket", basket_view, name="basket")
]
