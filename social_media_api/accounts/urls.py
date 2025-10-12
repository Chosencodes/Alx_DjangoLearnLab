from django.urls import path
from .views import RegisterView, CustomAuthToken, ProfileView, FollowToggleView, FollowListView, FollowUserView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowToggleView.as_view(), name='follow_toggle'),
    path('follows/', FollowListView.as_view(), name='follows_list'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
]
