# Update Book

from bookshelf.models import Book

# Retrieve the book

book = Book.objects.get(id=1)

# Update the title

book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output:

# <Book: Nineteen Eighty-Four by George Orwell (1949)>
