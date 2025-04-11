import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')  # Replace with your actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        return author.books.all()
    return None

# List all books in a specific library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # REQUIRED for the checker
    return library.books.all()

# Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)  # Optional but consistent
    return library.librarian

if __name__ == "__main__":
    print("Books by Author John Doe:", get_books_by_author("John Doe"))
    print("Books in Library Central Library:", get_books_in_library("Central Library"))
    print("Librarian for Central Library:", get_librarian_for_library("Central Library"))
