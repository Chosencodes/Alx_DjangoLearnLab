from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register,
    UserLoginView,
    UserLogoutView,
    admin_view,
    librarian_view,
    member_view,
)

urlpatterns = [
    # Book-related URLs
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Authentication URLs
    path("register/", register, name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),

    # Role-based access URLs
    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),
]
