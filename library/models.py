from django.db import models
from datetime import datetime as dt

from accounts.models import CustomUser


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    year_of_release = models.PositiveIntegerField(default=dt.now().year)
    serial_book_number = models.CharField(max_length=13)
    description = models.TextField(blank=True)
    no_copies = models.PositiveIntegerField(default=1)
    no_available = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title} - {self.author}"

class BorrowRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_of_borrowing = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)
    date_of_return = models.DateField(null=True, blank=True)

    def __str__(self):
        status = "Returned" if self.returned else "Borrowed"
        return f"{self.user} - {self.book.title} ({status})"