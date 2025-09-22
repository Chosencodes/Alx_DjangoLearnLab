# Retrieve Book

from bookshelf.models import Book

# Retrieve the created Book instance

book = Book.objects.get(id=1)

# Expected Output:

# <Book: 1984 by George Orwell (1949)>
