from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_protect
from django import forms
from .models import Book
from .forms import BookForm, ExampleForm  # Import these from forms.py

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

# Example Form View (for contact or feedback)
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data here (e.g., save to database or send email)
            return redirect('thank_you')  # Redirect after successful form submission
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/example_form.html', {'form': form})
