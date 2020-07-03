from django.shortcuts import render, redirect
from .models import Product
from .models import Comment
from .forms import CommentForm
from django.contrib import messages

def add_comment(request):
    if request.method == "POST":
        if CommentForm(request.POST).is_valid:
            product = Product.objects.get(pk=request.POST["pk"])
            Comment(user=request.user, product=product, content = request.POST["content"], stars=request.POST["stars"]).save()
            messages.success(request, "Komentarz dodano")
        else:
            messages.success(request, "Błąd")
    return redirect("shop:product", pk=request.POST["pk"])
