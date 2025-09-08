from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")   # show these columns
    list_filter = ("publication_year", "author")            # add filter sidebar
    search_fields = ("title", "author")                     # add search box
