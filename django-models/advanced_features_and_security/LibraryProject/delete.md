book.delete()

all_books = Book.objects.all()
print(list(all_books))  # Expected: []

