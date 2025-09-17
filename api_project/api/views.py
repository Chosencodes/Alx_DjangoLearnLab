from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# ListAPIView (existing)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer