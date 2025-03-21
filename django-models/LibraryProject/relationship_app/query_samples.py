import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.book_set.all()  # Ensuring we use the reverse relation
    except Author.DoesNotExist:
        return None

# List all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None

# Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return None

if __name__ == "__main__":
    print("Books by Author John Doe:", list(get_books_by_author("John Doe") or []))
    print("Books in Library Central Library:", list(get_books_in_library("Central Library") or []))
    print("Librarian for Central Library:", get_librarian_for_library("Central Library"))
