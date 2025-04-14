from django.db import models
<<<<<<< HEAD
from django.conf import settings
=======

# Create your models here.
>>>>>>> 51216ea (Initial commit)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
<<<<<<< HEAD
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]


=======

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
>>>>>>> 51216ea (Initial commit)
