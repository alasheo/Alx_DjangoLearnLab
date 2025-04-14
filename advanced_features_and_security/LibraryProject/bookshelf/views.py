from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Book List View
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Book Create View (for example)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Logic for creating a book
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        Book.objects.create(title=title, author=author, publication_year=publication_year)
    return render(request, 'create_book.html')

# Book Delete View (for example)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to book list after deletion
    return render(request, 'delete_book.html', {'book': book})


# Create your views here.
