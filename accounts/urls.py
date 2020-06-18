from django.contrib import admin
from django.urls import path, include
from .views import index_view, account_view

urlpatterns = [
    path("", index_view, name="index"),
    path("", include("django_registration.backends.activation.urls")),
    path("", include("django.contrib.auth.urls")),
    path("<username>", account_view, name="account")
]
