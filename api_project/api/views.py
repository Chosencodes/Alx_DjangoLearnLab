from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from .models import Book
from .serializers import BookSerializer

# ListAPIView: Only authenticated users can list books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Requires user to be logged in

# Custom permission: Only the owner of the book can edit or delete it
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user  # Check if the logged-in user is the owner

# ViewSet: Full CRUD operations on books
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsOwner]  # Authenticated users + ownership check

    # Optional: You could also add IsAdminUser for admin-only endpoints
    # permission_classes = [IsAdminUser]
