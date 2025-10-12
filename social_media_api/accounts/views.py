# accounts/views.py
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404

# Import for feed view
from rest_framework.generics import ListAPIView

# Import your serializers
from .serializers import RegisterSerializer, UserSerializer

# Import your Post model and serializer for FeedView
from posts.models import Post
from posts.serializers import PostSerializer

# Import pagination safely
try:
    from posts.pagination import StandardResultsSetPagination
except ImportError:
    # fallback if pagination not yet created
    from rest_framework.pagination import PageNumberPagination

    class StandardResultsSetPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'
        max_page_size = 100

User = get_user_model()

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        if target_user == request.user:
            return Response({"detail": "Cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.add(target_user)
        return Response({"status": "followed"}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        request.user.following.remove(target_user)
        return Response({"status": "unfollowed"}, status=status.HTTP_200_OK)

# ---------------- FOLLOW SYSTEM ---------------- #
class FollowToggleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, pk=user_id)
        if target == request.user:
            return Response({"detail": "Cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        if target in request.user.following.all():
            request.user.following.remove(target)
            action = 'unfollowed'
        else:
            request.user.following.add(target)
            action = 'followed'

            # Notification (optional, safe import)
            try:
                from notifications.models import Notification
                Notification.objects.create(
                    recipient=target,
                    actor=request.user,
                    verb='followed you'
                )
            except ImportError:
                pass

        return Response({"status": action}, status=status.HTTP_200_OK)


class FollowListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following = request.user.following.all()
        followers = request.user.followers.all()
        return Response({
            "following": [{"id": u.id, "username": u.username} for u in following],
            "followers": [{"id": u.id, "username": u.username} for u in followers],
        }, status=status.HTTP_200_OK)


# ---------------- FEED SYSTEM ---------------- #
class FeedView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        following_qs = user.following.all()
        return Post.objects.filter(author__in=following_qs).order_by('-created_at')


# ---------------- AUTH ---------------- #
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token, _ = Token.objects.get_or_create(user=user)
        response.data['token'] = token.key
        return response


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user_id": user.id,
                "username": user.username
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

