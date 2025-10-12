from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)


app_name = 'blog'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Login / Logout using Django built-in views with template overrides
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Blog Post CRUD URLs
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Comments
    path('post/<int:post_pk>/comments/new/', views.add_comment, name='comment_create'),
    path('post/<int:post_pk>/comments/<int:comment_pk>/edit/', views.edit_comment, name='comment_edit'),
    path('post/<int:post_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='comment_delete'),

] 


