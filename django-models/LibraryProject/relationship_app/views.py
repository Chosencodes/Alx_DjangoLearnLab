from django.shortcuts import render
from django.views.generic.detail import DetailView  # must be from detail
from .models import Book
from .models import Library  # keep separate lines since it works

# -------------------------
# Function-based view: list all books
# -------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# -------------------------
# Class-based view: details of a specific library
# -------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include all books that belong to this library
        context["books"] = Book.objects.filter(library=self.object)
        return context
