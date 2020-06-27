from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django_registration.views import RegistrationView, ActivationView

@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect("accounts:login")
