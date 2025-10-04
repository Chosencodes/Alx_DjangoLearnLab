from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # ===== Authentication URLs =====
    path("register/", views.register, name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),

    # ===== Blog Post URLs =====
    path("", views.PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/new/", views.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),

    # ===== Comment URLs =====
    path("posts/<int:post_id>/comments/new/", views.CommentCreateView.as_view(), name="comment_create"),
    path("comments/<int:pk>/edit/", views.CommentUpdateView.as_view(), name="comment_update"),
    path("comments/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment_delete"),
]
