from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileUpdateForm
from django.contrib import messages

@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")

def adress_update(request):
    form = ProfileUpdateForm(instance=request.user)
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid:
            form.save()
            messages.success(request, "Adres zmieniony")
        else:
            messages.warning(request, "Błąd")
        return redirect("profile")

    return render(request, "accounts/adress_update.html", {"form":form})

    




   

