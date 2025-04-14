from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_protect
from .models import Book
from django import forms
from .forms import BookForm

# --- Form class to validate inputs and avoid raw request.POST usage ---
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


# Book List View
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Safe ORM query
    return render(request, 'bookshelf/book_list.html', {'books': books})


# Book Create View
@permission_required('bookshelf.can_create', raise_exception=True)
@csrf_protect  # Ensure CSRF protection
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # Validate input
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})


# Book Delete View
@permission_required('bookshelf.can_delete', raise_exception=True)
@csrf_protect
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Safer than Book.objects.get
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to book list after deletion
    return render(request, 'bookshelf/delete_book.html', {'book': book})
