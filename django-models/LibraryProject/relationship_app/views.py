<<<<<<< HEAD
=======
<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======


# Create your views here.
>>>>>>> 74e4853 (add security)
from django.shortcuts import render
from django.views.generic import DetailView  # This import is correct
from .models import Book, Library  # Make sure both models exist

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
>>>>>>> 51216ea (Initial commit)
