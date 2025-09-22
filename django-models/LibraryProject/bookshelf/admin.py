from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # show these columns
    search_fields = ("title", "author")  # allow searching by title/author
    list_filter = ("publication_year",)  # add filter by year
