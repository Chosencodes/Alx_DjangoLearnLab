# Create

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

# <Book: 1984 by George Orwell (1949)>

# Retrieve

from bookshelf.models import Book

book = Book.objects.first()
book.title, book.author, book.publication_year

# ('1984', 'George Orwell', 1949)

# Update

book = Book.objects.first()
book.title = "Nineteen Eighty-Four"
book.save()
book.title

# 'Nineteen Eighty-Four'

# Delete

book = Book.objects.first()
book.delete()
Book.objects.all()

# <QuerySet []>
