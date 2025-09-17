from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # old list view
    path('api/', include(router.urls)),  # include the router URLs
    # path('api/', include('api.urls')),  # only if you have additional api urls
]
