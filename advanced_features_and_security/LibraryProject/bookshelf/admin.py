from django.contrib import admin
from .models import Author, Book, Library, Librarian


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date')
    list_filter = ('published_date', 'author')
    search_fields = ('title',)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')   # ✅ removed invalid "location"
    search_fields = ('name',)


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'library')
    search_fields = ('name',)
