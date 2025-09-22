# LibraryProject/relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # existing list view
    path('add_book/', views.add_book, name='add_book'),  # new add view
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),  # new edit view
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),  # new delete view
]
