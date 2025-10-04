from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post
from .forms import SignUpForm, ProfileForm, PostForm

# ===========================
# 🧩 AUTHENTICATION VIEWS
# ===========================

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in immediately after registration
            messages.success(request, "Registration successful. Welcome!")
            return redirect(reverse_lazy("blog:post_list"))
    else:
        form = SignUpForm()
    return render(request, "blog/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "blog/login.html"


class CustomLogoutView(LogoutView):
    template_name = "blog/logout.html"


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("blog:profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})


# ===========================
# 📝 BLOG POST CRUD VIEWS
# ===========================

# List all posts
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]


# View a single post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set author to logged-in user
        messages.success(self.request, "Post created successfully!")
        return super().form_valid(form)


# Update an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully!")
        return super().form_valid(form)


# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post deleted successfully!")
        return super().delete(request, *args, **kwargs)
