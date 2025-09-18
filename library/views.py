from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from library.models import Book, BorrowRecord
from datetime import datetime as dt, timedelta


# Create your views here.

def landing(request):
    return render(request, "library/landing.html", {})

@login_required
def home(request):
    if not request.user.is_approved:
        print("Your account is awaiting admin approval.")
        return redirect("pending")
    if request.method == "POST" and request.POST.get("borrow"):
        handle_borrow_request(request, request.POST.get("borrow"))
    books = Book.objects.all()
    return render(request, "library/home.html", {"books": books})

@login_required
def book(request, id):
    if not request.user.is_approved:
        print("Your account is awaiting admin approval.")
        return redirect("pending")
    if request.method == "POST" and request.POST.get("borrow"):
        handle_borrow_request(request, request.POST.get("borrow"))
    book_obj = get_object_or_404(Book, id=id)
    return render(request, "library/book.html", {"book": book_obj})

@login_required
def borrowed(request):
    if not request.user.is_approved:
        print("Your account is awaiting admin approval.")
        return redirect("pending")
    brs = request.user.borrowrecord_set.all()
    return render(request, "library/borrowed.html", {"brs": brs})

@login_required
def history(request):
    if not request.user.is_approved:
        print("Your account is awaiting admin approval.")
        return redirect("pending")
    brs = request.user.borrowrecord_set.all()
    return render(request, "library/history.html", {"brs": brs})


def handle_borrow_request(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.no_available > 0:
        book.no_available -= 1
        book.save()
        borrow_book(request.user, book)
        return True
    else:
        print(request, "We're sorry, there are no more copies of this book available.")
        return False

def borrow_book(user, b_book):
    br = BorrowRecord(user=user,
                      book = b_book,
                      due_date = dt.now() + timedelta(days=14))
    br.save()