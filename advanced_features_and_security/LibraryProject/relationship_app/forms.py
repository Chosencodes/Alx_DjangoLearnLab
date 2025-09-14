from django import forms
from bookshelf.models import Book   # import Book from bookshelf app

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
