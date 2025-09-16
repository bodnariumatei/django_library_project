from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True   # allow login system-wise
            user.is_approved = False # but require admin approval
            user.save()
            messages.info(request, "Your account has been created. Wait for admin approval.")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def pending(request):
    return render(request, "accounts/pending.html")

@login_required()
def logged_out(request):
    auth_logout(request)
    return render(request, 'accounts/logged_out.html')

def redirecting(request):
    if request.user.is_staff:
        return redirect("/admin")
    else:
        return redirect("/library/home")