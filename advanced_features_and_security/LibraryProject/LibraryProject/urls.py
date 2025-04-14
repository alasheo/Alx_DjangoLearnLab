from django.contrib import admin
from django.urls import path
from bookshelf import views  # Ensure you're importing from the 'bookshelf' app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('example/', views.example_form_view, name='example_form'),  # Add this line for the example form
]
