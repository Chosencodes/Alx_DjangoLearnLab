from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Posts
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Comments
    path('posts/<int:post_id>/comments/new/', views.comment_create, name='comment_create'),
    path('comments/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]
