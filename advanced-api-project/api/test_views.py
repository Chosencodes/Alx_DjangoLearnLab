from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create an author and a book
        self.author = Author.objects.create(name='J.K. Rowling')
        self.book = Book.objects.create(title='Harry Potter', publication_year=2000, author=self.author)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'New Book',
            'publication_year': 2025,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {'title': 'Updated Title', 'publication_year': 2001, 'author': self.author.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        url = reverse('book-list') + '?title=Harry Potter'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Harry'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        Book.objects.create(title='Another Book', publication_year=1999, author=self.author)
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1999)
