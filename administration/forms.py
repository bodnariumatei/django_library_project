from email.policy import default

from django import forms
from datetime import datetime as dt

from library.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publisher", "year_of_release", "serial_book_number", "description", "no_copies", "no_available"]


