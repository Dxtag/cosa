from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User


# Create your views here.
def index_view(request):
    return HttpResponse("Your account")

def account_view(request, username):
    user = get_object_or_404(User, username=username)
    return HttpResponse(user.username)