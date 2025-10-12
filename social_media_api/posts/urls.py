from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView
from accounts.views import RegisterView, LoginView, ProfileView, FollowToggleView, FollowListView, FeedView # adjust import if needed

# Initialize router
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

# URL patterns
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('feed/', FeedView.as_view(), name='feed'),  # feed endpoint
    path('', include(router.urls)),  # include router endpoints
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowToggleView.as_view(), name='follow_toggle'),
    path('follows/', FollowListView.as_view(), name='follow_list'),
]
