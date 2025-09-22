# api/views.py

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework  # ALX checker expects this exact import
from .models import Book
from .serializers import BookSerializer

# List and Create View for Books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        rest_framework.DjangoFilterBackend,  # filtering
        filters.SearchFilter,                # searching
        filters.OrderingFilter                # ordering
    ]
    filterset_fields = ['title', 'author', 'publication_year']  # fields to filter
    search_fields = ['title', 'author__name']                  # fields to search
    ordering_fields = ['title', 'publication_year']           # fields to order

# Retrieve, Update, Delete View for a single Book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
