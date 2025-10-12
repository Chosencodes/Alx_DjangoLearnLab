from django.urls import path
from .views import RegisterView, CustomAuthToken
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', RegisterView.as_view(), name='profile'),  # placeholder, can update later
]
