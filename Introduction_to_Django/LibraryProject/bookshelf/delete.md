# Delete Book

from bookshelf.models import Book

# Retrieve the book

book = Book.objects.get(id=1)

# Delete it

book.delete()

# Expected Output:

# (1, {'bookshelf.Book': 1})

# Confirm deletion

Book.objects.all()

# Expected Output:

# <QuerySet []>
