from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileForm
from django.urls import reverse_lazy
from django.contrib import messages

# Registration view (function-based)
def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in immediately after registration
            messages.success(request, "Registration successful. Welcome!")
            return redirect(reverse_lazy("blog:post_list"))
    else:
        form = SignUpForm()
    return render(request, "blog/register.html", {"form": form})

# Log in: use Django's class-based LoginView
class CustomLoginView(LoginView):
    template_name = "blog/login.html"

# Logout: use Django's LogoutView
class CustomLogoutView(LogoutView):
    template_name = "blog/logout.html"

# Profile view to view/edit own profile
@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("blog:profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})
