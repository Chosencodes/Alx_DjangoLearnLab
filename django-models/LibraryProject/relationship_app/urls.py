from django.urls import path
from .views import (
    list_books,  # function-based book list
    LibraryDetailView,  # class-based library detail
    home_view,
    register_view, CustomLoginView, CustomLogoutView
)

urlpatterns = [
    path('', home_view, name='home'),
    path('books/', list_books, name='list_books'),  # updated
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]


urlpatterns += [
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
