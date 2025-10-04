from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # your blog views, e.g.:
    # path("", views.post_list, name="post_list"),

    # auth
    path("register/", views.register, name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
    path("posts/", views.PostListView.as_view(), name="post_list"),               # /posts/
    path("posts/new/", views.PostCreateView.as_view(), name="post_create"),      # /posts/new/
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"), # /posts/<pk>/
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"), # /posts/<pk>/edit/
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"), # /posts/<pk>/delete/
]
