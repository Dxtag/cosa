from django.urls import path
from .views import IndexView, product_view, basket_view, add_to_basket

app_name = "shop"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("product/<int:pk>", product_view, name="product"),
    path("basket", basket_view, name="basket"),
    path("product/<int:pk>/add/<int:quantity>", add_to_basket, name="add_to_basket"),
]
