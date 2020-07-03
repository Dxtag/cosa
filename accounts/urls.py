from django.contrib import admin
from django.urls import path, include
from .views import profile_view, adress_update

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", include('django_registration.backends.activation.urls')),
    path("profile/", profile_view , name="profile"),
    path("profile/adress_update",adress_update , name="adress_update")
]
