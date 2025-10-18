from rest_framework.routers import DefaultRouter
from django.urls import path, include

# Import views
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView
from accounts.views import RegisterView, LoginView, ProfileView, FollowToggleView, FollowListView

# Initialize router for posts and comments
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

# URL patterns
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Feed endpoint
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),      # ✅ required
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),# ✅ required

    # Follow/unfollow endpoints
    path('follow/<int:user_id>/', FollowToggleView.as_view(), name='follow_toggle'),
    path('follows/', FollowListView.as_view(), name='follow_list'),

    # Include router URLs for posts and comments
    path('', include(router.urls)),
]
