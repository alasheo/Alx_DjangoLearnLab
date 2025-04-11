import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  # Replace with your actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # ✅ REQUIRED
    return Book.objects.filter(author=author)       # ✅ REQUIRED

# List all books in a specific library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # REQUIRED
    return library.books.all()

# Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)  # REQUIRED
    librarian = Librarian.objects.get(library=library)  # ✅ REQUIRED
    return librarian

if __name__ == "__main__":
    print("Books by Author John Doe:", get_books_by_author("John Doe"))
    print("Books in Library Central Library:", get_books_in_library("Central Library"))
    print("Librarian for Central Library:", get_librarian_for_library("Central Library"))
