from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Simple ListAPIView (for listing only)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Full CRUD operations using ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
