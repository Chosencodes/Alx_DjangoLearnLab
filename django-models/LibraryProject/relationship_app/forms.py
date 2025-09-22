# relationship_app/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'library', 'isbn', 'copies_available']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }

