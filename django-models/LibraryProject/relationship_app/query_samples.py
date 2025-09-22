from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "George Orwell"
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:", list(books_by_author))

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}:", list(books_in_library))

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}:", librarian.name)
